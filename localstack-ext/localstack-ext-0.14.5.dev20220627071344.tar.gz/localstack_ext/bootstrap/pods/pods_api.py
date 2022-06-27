_D=False
_C='rb'
_B=True
_A=None
import hashlib,json,logging,os,zipfile
from typing import Any,Dict,List,Optional,Set,Tuple
from localstack.constants import TEST_AWS_ACCOUNT_ID
from localstack.utils.common import cp_r,mkdir,rm_rf,save_file,short_uid,to_str
from localstack.utils.files import load_file
from localstack.utils.http import safe_requests
from localstack_ext.bootstrap.pods.constants import NIL_PTR,VERSION_SPACE_ARCHIVE
from localstack_ext.bootstrap.pods.models import Commit,Revision,Serialization,StateFileRef,Version
from localstack_ext.bootstrap.pods.object_storage import get_object_storage_provider
from localstack_ext.bootstrap.pods.servicestate.service_state import ServiceState
from localstack_ext.bootstrap.pods.servicestate.service_state_types import BackendState,ServiceKey
from localstack_ext.bootstrap.pods.utils.adapters import ServiceStateMarshaller
from localstack_ext.bootstrap.pods.utils.common import PodsConfigContext,zip_directories
from localstack_ext.bootstrap.pods.utils.hash_utils import compute_file_hash,compute_revision_hash,random_hash
from localstack_ext.bootstrap.pods.utils.metamodel_utils import CommitMetamodelUtils,MetamodelDelta,MetamodelDeltaMethod
from localstack_ext.bootstrap.pods.utils.remote_utils import extract_meta_and_state_archives,merge_version_space,register_remote
from localstack_ext.bootstrap.state_utils import API_STATES_DIR,DYNAMODB_DIR,KINESIS_DIR
from localstack_ext.utils.persistence import marshall_backend,unmarshall_backend
LOG=logging.getLogger(__name__)
ROOT_DIR_LOOKUP={str(Serialization.KINESIS):KINESIS_DIR,str(Serialization.DDB):DYNAMODB_DIR,str(Serialization.MAIN):API_STATES_DIR}
class PodsApi:
	def __init__(A,config_context):A.config_context=config_context;A.object_storage=get_object_storage_provider(A.config_context);A.commit_metamodel_utils=CommitMetamodelUtils(A.config_context)
	def init(A,pod_name=_A):
		C=pod_name;C=C or A.config_context.pod_name
		if A.config_context.pod_exists_locally(pod_name=C):LOG.warning(f"Pod with name {C} already exists locally");return
		mkdir(A.config_context.get_pod_root_dir());mkdir(A.config_context.get_versions_path());mkdir(A.config_context.get_delta_log_path());A.config_context.set_pod_context(C);F=random_hash();G=random_hash();E=Revision(hash_ref=F,parent_ptr=NIL_PTR,creator=A.config_context.get_context_user(),rid=short_uid(),revision_number=0,state_files=set());B=Version(hash_ref=G,parent_ptr=NIL_PTR,creator=A.config_context.get_context_user(),comment='Initial version',outgoing_revision_ptrs={F},incoming_revision_ptr=_A,state_files=set(),version_number=Version.DEFAULT_INITIAL_VERSION_NUMBER);B.revisions.append(E);A.object_storage.upsert_objects(B)
		with open(A.config_context.get_head_path(),'w')as D:D.write(str(B.version_number))
		with open(A.config_context.get_max_ver_path(),'w')as D:D.write(str(B.version_number))
		with open(A.config_context.get_known_ver_path(),'w')as D:D.write(str(B.version_number))
		A.config_context.update_ver_log(author=A.config_context.get_context_user(),ver_no=B.version_number,rev_id=E.rid,rev_no=E.revision_number);LOG.debug('Successfully initialized cloud pod under %s',A.config_context.get_pod_root_dir())
	def init_remote(A,version_space_archive,meta_archives,state_archives,remote_info,pod_name):
		B=version_space_archive;mkdir(A.config_context.get_pod_root_dir());A.config_context.set_pod_context(pod_name=pod_name)
		with zipfile.ZipFile(B)as C:C.extractall(A.config_context.get_pod_root_dir());LOG.debug('Successfully extracted version space zip')
		rm_rf(B);extract_meta_and_state_archives(meta_archives=meta_archives,state_archives=state_archives,config_context=A.config_context);D=A._get_max_version()
		with open(A.config_context.get_head_path(),'w')as E:E.write(str(D.version_number))
		register_remote(remote_info=remote_info,config_context=A.config_context)
	def commit(D,message=_A):
		A,B=D._get_expansion_point_with_head();E=compute_revision_hash(A,D.config_context.get_obj_store_path())
		if A.parent_ptr!=NIL_PTR:F=B.get_revision(A.parent_ptr);F.assoc_commit.head_ptr=E
		B.update_revision_key(old_key=A.hash_ref,new_key=E);A.hash_ref=E;C=Revision(hash_ref=random_hash(),state_files=set(),parent_ptr=E,creator=A.creator,rid=short_uid(),revision_number=A.revision_number+1);B.revisions.append(C);G=Commit(tail_ptr=A.hash_ref,head_ptr=C.hash_ref,message=message);A.assoc_commit=G;D.object_storage.upsert_objects(B);D.config_context.update_ver_log(author=C.creator,ver_no=B.version_number,rev_id=C.rid,rev_no=C.revision_number);return A
	def merge_from_remote(A,version_space_archive,meta_archives,state_archives):merge_version_space(version_space_archive,config_context=A.config_context);extract_meta_and_state_archives(meta_archives=meta_archives,state_archives=state_archives,config_context=A.config_context)
	def is_remotely_managed(A):return A.config_context.is_remotely_managed()
	def rename_pod(B,new_pod_name):
		A=new_pod_name
		if B.config_context.pod_exists_locally(A):LOG.warning(f"{A} already exists locally");return _D
		B.config_context.rename_pod(A);return _B
	def list_locally_available_pods(A,show_remote_or_local=_B):
		mkdir(A.config_context.cloud_pods_root_dir);C=[B for B in os.listdir(A.config_context.cloud_pods_root_dir)if not B.endswith('.json')]
		if not show_remote_or_local:return set(C)
		D=set()
		for B in C:E=f"remote/{B}"if A.config_context.is_remotely_managed(B)else f"local/{B}";D.add(E)
		return D
	def push(A,comment=_A):
		B,D=A._get_expansion_point_with_head();I=A._get_max_version();F=D.version_number;G=I.version_number;J=G+1;H=A._create_service_state_from_state_file_refs(state_file_refs=B.state_files)
		if F!=G:A.merge_expansion_point_with_max(H);F=G
		K=A.config_context.get_version_state_archive_path(F);ServiceStateMarshaller.marshall_zip_archive(file_path=K,service_state=H);D.hash_ref=H.compute_hash_on_state();E=Revision(hash_ref=random_hash(),state_files=B.state_files,parent_ptr=NIL_PTR,creator=B.creator,rid=short_uid(),revision_number=0);C=Version(hash_ref=random_hash(),state_files=set(),parent_ptr=I.hash_ref,creator=B.creator,comment=comment,outgoing_revision_ptrs={E.hash_ref},incoming_revision_ptr=B.hash_ref,version_number=J);C.revisions.append(E);L=Commit(tail_ptr=B.hash_ref,head_ptr=C.hash_ref,message='Finalizing commit');B.state_files=C.state_files;B.assoc_commit=L;A.object_storage.upsert_objects(D,C);A._update_head(C.version_number);A._update_max_ver(C.version_number);A._add_known_ver(C.version_number);M=A.config_context.metamodel_file(B.revision_number);A.commit_metamodel_utils.create_metamodel_archive(D,overwrite=_B,metamodels_file=M);A.config_context.update_ver_log(author=B.creator,ver_no=C.version_number,rev_id=E.rid,rev_no=E.revision_number);return C
	def set_pod_context(A,pod_name):A.config_context.set_pod_context(pod_name)
	def add_metamodel_to_current_revision(A,metamodel):B,C=A._get_expansion_point_with_head();D=json.dumps(metamodel);E=A._create_state_file_from_blob(D);B.metamodel_file=E;A.object_storage.upsert_objects(C)
	def get_revision_metamodel(C,revision=_A):
		A=revision
		if not A:A,E=C._get_expansion_point_with_head()
		if not A.metamodel_file:return{}
		D=C.config_context.get_obj_file_path(A.metamodel_file);B=load_file(D);B=json.loads(to_str(B));return B
	def create_state_file_from_fs(B,file_name,service,region,root,serialization=Serialization.MAIN,account_id=TEST_AWS_ACCOUNT_ID,object=_A,rel_path=_A):E=account_id;D=region;C=service;A=hashlib.sha1(object).hexdigest();F=B.config_context.get_obj_file_path(A);save_file(file=F,content=object);G=StateFileRef(hash_ref=A,rel_path=rel_path or f"{root}/{E}/{C}/{D}",file_name=file_name,size=len(object),service=C,region=D,account_id=E,serialization=serialization);B._add_state_file_to_expansion_point(G);return A
	def _create_state_file_from_blob(C,blob):
		A=blob;E=random_hash();B=C.config_context.get_obj_file_path(E)
		if not isinstance(A,(str,bytes)):A=marshall_backend(A)
		save_file(B,A);D=compute_file_hash(B);F=C.config_context.get_obj_file_path(D);os.rename(B,F);return D
	def _get_state_file_path(B,key):
		A=B.config_context.get_obj_file_path(key)
		if os.path.isfile(A):return A
		LOG.warning(f"No state file with found with key: {key}")
	def _add_state_file_to_expansion_point(A,state_file):B=state_file;C,E=A._get_expansion_point_with_head();D=set(filter(lambda sf:not sf.congruent(B),C.state_files));D.add(B);C.state_files=D;A.object_storage.upsert_objects(E)
	def create_version_space_archive(A):
		B=os.path.join(A.config_context.get_pod_root_dir(),VERSION_SPACE_ARCHIVE);rm_rf(B);C=zip_directories(zip_dest=B,directories=A.config_context.get_version_space_dir_paths())
		with zipfile.ZipFile(C,'a')as E:
			for D in A.config_context.get_version_space_file_paths():E.write(D,arcname=os.path.basename(D))
		return C
	def get_head(A):return A.object_storage.get_version(A.config_context.get_head_version_number())
	def _get_max_version(A):return A.object_storage.get_version(A.config_context.get_max_version_number())
	def get_max_version_no(A):
		with open(A.config_context.get_max_ver_path())as B:return int(os.path.basename(B.readline()))
	def _get_expansion_point_with_head(B):A=B.get_head();C=A.get_latest_revision();return C,A
	def push_overwrite(A,version,comment):
		B=version;D,H=A._get_expansion_point_with_head()
		if B>A.get_max_version_no():LOG.debug('Attempted to overwrite a non existing version.. Aborting');return _D
		C=A.get_version_by_number(B);E=A._create_service_state_from_state_file_refs(state_file_refs=D.state_files);F=A.config_context.get_version_state_archive_path(B);ServiceStateMarshaller.marshall_zip_archive(file_path=F,service_state=E);G=A.config_context.metamodel_file(D.revision_number);A.commit_metamodel_utils.create_metamodel_archive(C,overwrite=_B,metamodels_file=G);C.comment=comment;A.object_storage.upsert_objects(C);return _B
	def _add_assets_to_version_state_archive(A,version_number,cleanup=_B):
		D=A.config_context.get_version_state_archive_path(version=version_number);B=A.config_context.get_assets_root_path()
		with zipfile.ZipFile(D,'a')as E:
			for (F,I,G) in os.walk(B):
				for H in G:C=os.path.join(F,H);E.write(filename=C,arcname=os.path.relpath(C,start=A.config_context.get_pod_root_dir()))
		if cleanup:rm_rf(B)
	@staticmethod
	def _get_dst_path_for_state_file(version_state_dir,state_file):
		C=version_state_dir;A=state_file
		if A.serialization in[str(Serialization.KINESIS),str(Serialization.DDB)]:B=os.path.join(C,ROOT_DIR_LOOKUP[str(A.serialization)])
		else:B=os.path.join(C,ROOT_DIR_LOOKUP[str(A.serialization)],A.rel_path)
		mkdir(B);return B
	def _create_service_state_from_state_file_refs(C,state_file_refs):
		A=ServiceState()
		for B in state_file_refs:
			D=B.rel_path.startswith('api_states')
			if D:A.put_backend(C._create_backend_state_from_state_file(B))
			else:C._add_assets_from_state_file(B,A)
		return A
	def _create_backend_state_from_state_file(B,state_file):A=state_file;C=ServiceKey(account_id=A.account_id,region=A.region,service=A.service);D=B.object_storage.get_state_file_location_by_key(A.hash_ref);E=unmarshall_backend(load_file(file_path=D,mode=_C));return BackendState(key=C,backends={A.file_name:E})
	def _add_assets_from_state_file(B,state_file,service_state):A=state_file;C=B.object_storage.get_state_file_location_by_key(A.hash_ref);D=load_file(file_path=C,mode=_C);service_state.put_asset(service_name=A.service,asset_name=A.rel_path,asset_value=D)
	def set_active_version(A,version_no,commit_before=_D):
		B=version_no;C=A.config_context.list_known_versions()
		for D in C:
			if D==B:
				if commit_before:A.commit()
				A._set_active_version(B);return _B
		LOG.info(f"Version with number {B} not found");return _D
	def _set_active_version(A,version_no):
		C=version_no;D=A.get_head()
		if D.version_number!=C and A.object_storage.version_exists(D.version_number):
			B=A.object_storage.get_version(C);A._update_head(B.version_number)
			if B.active_revision_ptr==NIL_PTR:E=Revision(hash_ref=random_hash(),state_files=set(),parent_ptr=NIL_PTR,creator=A.config_context.get_context_user(),rid=short_uid(),revision_number=0);B.revisions.append(E);B.outgoing_revision_ptrs.add(E.hash_ref);A.object_storage.upsert_objects(B)
	def get_version_by_number(B,version_no):
		A=version_no;C=B.config_context.list_known_versions()
		if A not in C:LOG.warning('Could not find version number %s',A);return
		return B.object_storage.get_version(A)
	def list_versions(A):B=A.config_context.list_known_versions();C=[A.object_storage.get_version(C)for C in B];return C
	def get_version_summaries(A):
		def B(version):A=version;return f"{A.version_number}, {A.creator}, {A.comment}"
		C=A.list_versions();D=[B(A)for A in C];return D
	def list_version_commits(C,version_no):
		D=version_no
		if D==-1:A=C._get_max_version()
		else:A=C.get_version_by_number(D)
		if not A:return[]
		E=[];B=A.get_revision(A.incoming_revision_ptr)
		if not B:B=A.revisions[0]
		while B:
			F=B.assoc_commit
			if F:E.append(F)
			B=A.get_revision(B.parent_ptr)
		return E
	def _update_head(B,new_head_ver_no):
		A=new_head_ver_no
		with open(B.config_context.get_head_path(),'w')as C:C.write(str(A));return str(A)
	def _update_max_ver(B,new_max_ver_no):
		A=new_max_ver_no
		with open(B.config_context.get_max_ver_path(),'w')as C:C.write(str(A));return str(A)
	def _add_known_ver(B,new_ver_no):
		A=new_ver_no
		with open(B.config_context.get_known_ver_path(),'a')as C:C.write(f"\n{A}");return str(A)
	def merge_expansion_point_with_max(A,current):
		C=current;F=A.get_max_version_no()-1;D=A.get_head().version_number;LOG.debug('Merge expansion point with max. Services in the new version service state = %s',C.get_services());G=A.config_context.get_version_state_archive(F);E=ServiceStateMarshaller.unmarshall(zipfile.ZipFile(G));LOG.debug('Merge expansion point with max. Services in the max service state = %s',E.get_services());B=_A
		if D>Version.DEFAULT_INITIAL_VERSION_NUMBER:H=A.config_context.get_version_state_archive(D);B=ServiceStateMarshaller.unmarshall(zipfile.ZipFile(H));LOG.debug('Merge expansion point with max. Services in the ancestor service state = %s',B.get_services())
		C.merge(E,B)
	def add_assets_to_pod(B,assets_root_paths):
		for A in assets_root_paths:
			C=os.path.join(B.config_context.get_assets_root_path(),os.path.basename(A))
			try:cp_r(src=A,dst=C)
			except Exception as D:LOG.warning('Failed to copy assets for %s: %s',A,D)
	def create_delta_log(A,state_from,state_to,diff_method=MetamodelDeltaMethod.SIMPLE):
		try:C=MetamodelDelta.get(diff_method);return C.create_delta_log(state_from,state_to,A.config_context)
		except Exception as D:LOG.debug('Unable to create delta log for version graph nodes: %s',D);B=short_uid();E=os.path.join(A.config_context.get_delta_log_path(),B);save_file(E,'{}');return B
	def upload_version_and_product_space(A,presigned_urls):
		C=presigned_urls
		def B(pre_signed_url,zip_data_content):
			A=safe_requests.put(pre_signed_url,data=zip_data_content)
			if A.status_code>=400:raise Exception(f"Unable to upload pod state to S3 (code {A.status_code}): {A.content}")
			return A
		G=C.get('presigned_version_space_url');D=A.create_version_space_archive()
		with open(D,_C)as H:B(G,H.read())
		I=C.get('presigned_meta_state_urls');rm_rf(D)
		for (E,F) in I.items():
			J=F['meta'];K=A.config_context.get_version_meta_archive(E)
			with open(K,_C)as L:B(J,L)
			M=F['state'];N=A.config_context.get_version_state_archive(E)
			with open(N,_C)as O:B(M,O)