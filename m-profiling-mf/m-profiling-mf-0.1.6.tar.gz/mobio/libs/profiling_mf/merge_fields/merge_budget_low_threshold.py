from mobio.libs.profiling_mf.merge_fields.base_merge import BaseMerge, MergeListGroup


class MergeBudgetLowThreshold(BaseMerge):
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
        suggest = (
            True
            if isinstance(profile_data, int) and self.field_key not in set_suggest_fields
            else False
        )
        if suggest:
            set_suggest_fields.add(self.field_key)
        field_value = self.__build_value__(value=profile_data, suggest=suggest, predict=predict)
        suggest_data[self.field_key] = self.build_merge_data(
            translate_key=translate_key,
            field_property=field_property,
            display_type=display_type,
            displayable=False,
            editable=False,
            mergeable=False,
            order=1,
            group=MergeListGroup.DYNAMIC,
            value=field_value,
        )

    def set_filter_value(self, suggest_filter_data, profile_data):
        pass

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
        suggest = True if isinstance(origin_data, int) and self.field_key not in set_suggest_fields else False
        if suggest:
            set_suggest_fields.add(self.field_key)
        field_value = self.__build_value__(value=origin_data, suggest=suggest)
        suggest_data[self.field_key] = self.build_merge_data(
            translate_key=translate_key,
            field_property=field_property,
            display_type=display_type,
            displayable=False,
            editable=False,
            mergeable=False,
            order=1,
            group=MergeListGroup.DYNAMIC,
            value=field_value,
        )

    def merge_data(self, target_data, source_data, is_master_data=False):
        if source_data:
            suggest = source_data.get("field_value").get("suggest")
            value = source_data.get("field_value").get("value")
            if suggest and value is not None:
                target_data[self.field_key] = value
