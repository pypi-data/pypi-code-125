from mobio.libs.profiling_mf.merge_fields.base_merge import BaseMerge, MergeListGroup


class MergeIsp(BaseMerge):
    def serialize_data(
        self,
        suggest_data,
        profile_data,
        set_suggest_fields,
        set_unique_suggest_values,
        field_property,
        display_type,
        translate_key,
        predict=None
    ):
        lst_suggest_face_id = []
        set_isp = set()
        profile_data = profile_data if profile_data is not None else []
        for isp in profile_data:
            if isp not in set_isp:
                lst_suggest_face_id.append(
                    self.__build_value__(value=isp, suggest=True, changealbe=False)
                )
                set_isp.add(isp)
        suggest_data[self.field_key] = self.build_merge_data(
            translate_key=translate_key,
            field_property=field_property,
            display_type=display_type,
            displayable=True,
            editable=False,
            mergeable=True,
            order=1,
            group=MergeListGroup.INFORMATION,
            value=lst_suggest_face_id,
        )

    def set_filter_value(self, suggest_filter_data, profile_data):
        profile_data = profile_data if profile_data is not None else []
        for face_id in profile_data:
            if face_id:
                suggest_filter_data.add(face_id)

    def serialize_origin_data(
        self,
        suggest_data,
        origin_data,
        set_suggest_fields,
        set_unique_suggest_values,
        field_property,
        display_type,
        translate_key,
    ):
        lst_suggest_face_id = []
        set_isp = set()
        origin_data = origin_data if origin_data is not None else []
        for isp in origin_data:
            if isp not in set_isp:
                lst_suggest_face_id.append(
                    self.__build_value__(value=isp, suggest=True, changealbe=False)
                )
                set_isp.add(isp)
        suggest_data[self.field_key] = self.build_merge_data(
            translate_key=translate_key,
            field_property=field_property,
            display_type=display_type,
            displayable=True,
            editable=False,
            mergeable=True,
            order=1,
            group=MergeListGroup.INFORMATION,
            value=lst_suggest_face_id,
        )

    def merge_data(self, target_data, source_data, is_master_data=False):
        if source_data:
            target_data[self.field_key] = target_data.get(self.field_key) if target_data.get(self.field_key) else []
            set_isp = set(target_data.get(self.field_key)) if not is_master_data else set()
            for isp in source_data.get('field_value'):
                if isp.get("suggest"):
                    set_isp.add(isp.get("value"))
            target_data[self.field_key] = list(set_isp)
