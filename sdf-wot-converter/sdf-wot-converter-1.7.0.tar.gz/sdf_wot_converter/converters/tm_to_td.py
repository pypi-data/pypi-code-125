from typing import (
    Dict,
)
import copy
import json_merge_patch
from jsonpointer import resolve_pointer

from .utility import ensure_value_is_list
from ..validation import validate_thing_description, validate_thing_model
from .wot_common import (
    is_thing_collection,
    replace_placeholders,
    resolve_extension,
    resolve_sub_things,
)


def replace_type(thing_description: Dict):
    json_ld_type = ensure_value_is_list(thing_description["@type"])
    result = list(filter(lambda item: item != "tm:ThingModel", json_ld_type))
    if len(result) == 0:
        del thing_description["@type"]
        return

    thing_description["@type"] = result


def _replace_version(partial_td):
    version = partial_td.get("version")

    if version is None:
        return

    if "model" in version and "instance" not in version:
        version["instance"] = version["model"]


def assert_tm_required(partial_td):
    if "tm:required" not in partial_td:
        return

    for required_affordance_pointer in partial_td["tm:required"]:
        root, pointer = tuple(required_affordance_pointer.split("#", 1))
        assert root == ""
        assert resolve_pointer(partial_td, pointer, None) is not None

    del partial_td["tm:required"]


def _replace_meta_data(partial_td, meta_data) -> Dict:
    if meta_data is None:
        return partial_td

    return json_merge_patch.merge(partial_td, meta_data)


def _replace_bindings(partial_td, bindings) -> Dict:
    if bindings is None:
        return partial_td

    return json_merge_patch.merge(partial_td, bindings)


def _resolve_submodels(thing_model: dict, thing_collection: dict):
    links = thing_model.get("links")

    if links is None:
        return

    for link in links:
        if link.get("rel") == "tm:submodel":
            # TODO: Apply proper mapping
            link["rel"] = "item"


def convert_tm_collection_to_td_collection(thing_collection):
    result = {}

    for key, value in thing_collection.items():
        _resolve_submodels(value, result)
        result[key] = convert_tm_to_td(value)

    return result


def convert_tm_to_td(
    thing_model: Dict,
    placeholder_map=None,
    meta_data=None,
    bindings=None,
    root_model_key="root",
) -> Dict:
    if is_thing_collection(thing_model):
        return convert_tm_collection_to_td_collection(thing_model)

    sub_models = resolve_sub_things(thing_model, replace_href=True)
    if len(sub_models) > 0:
        sub_models[root_model_key] = thing_model
        for key, value in sub_models.items():
            sub_models[key] = resolve_extension(value, resolve_relative_pointers=True)
        return convert_tm_collection_to_td_collection(sub_models)

    validate_thing_model(thing_model)
    partial_td: Dict = copy.deepcopy(thing_model)

    partial_td = resolve_extension(partial_td)
    partial_td = _replace_meta_data(partial_td, meta_data)
    partial_td = _replace_bindings(partial_td, bindings)

    replace_type(partial_td)

    partial_td = replace_placeholders(partial_td, placeholder_map)

    _replace_version(partial_td)

    assert_tm_required(partial_td)

    validate_thing_description(partial_td)

    return partial_td
