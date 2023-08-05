from de_utils.engineering_utils._schema_manager import SchemaManager
from de_utils.engineering_utils._fwf_loader import FwfColumnMetadata


class FwfSchemaManager(SchemaManager):
    """A class used to create and reach schemas for fixed withd files.

    Inherits SchemaManager.

    fwf = FwfSchemaManager()
    fwf.all_cols = ["a", "b"]
    fwf.column_idx = [[1,3], [4,6]]
    fwf.schema
    {
     'a': {'distinct': False,
           'dtype': StringType,
           'end': 3,
           'ignore': False,
           'lower': False,
           'nullable': True,
           'regex_replace': None,
           'snapshot_raw': False,
           'start': 1,
           'upper': False,
           'valid_regex': None,
           'valid_values': None},
     'b': {'distinct': False,
           'dtype': StringType,
           'end': 6,
           'ignore': False,
           'lower': False,
           'nullable': True,
           'regex_replace': None,
           'snapshot_raw': False,
           'start': 4,
           'upper': False,
           'valid_regex': None,
           'valid_values': None}}
    """

    __doc__ += SchemaManager.__doc__

    _default_item = {
        k: v
        for (k, v) in FwfColumnMetadata("", start=1, end=1).schema.items()}

    def _assert_non_zero_width(self, index_list):
        if not all((x[1] - x[0]) >= 0 for x in index_list):
            raise ValueError("end must be greater than"
                             " or equal to start")

    def _assert_not_overlapping(self, index_list):
        if not all(max(x) <= min(y) for
                   x, y in zip(index_list, index_list[1:])):
            raise ValueError("Column indexes must not overlap")

    def _assert_all_positive(self, *args):
        if not all(x > 0 for x in args):
            raise ValueError("All values must be positive, n>0")

    def _assert_all_int(self, *args):
        if not all(isinstance(x, int) for x in args):
            raise TypeError("All args must be of type int")

    def _assert_list_of_lists(self, lst):
        if not all(isinstance(elem, list) for elem in lst):
            raise TypeError("lst must be a list of lists")

    def _assert_length_two(self, *args):
        if not all(len(x) == 2 for x in args):
            raise ValueError("There must be two indexes for each column")

    def _assert_correct_len(self, index_list):
        n_schema = len(self.schema.keys())
        n_idx = len(index_list)
        if not n_idx == n_schema:
            raise ValueError(
                f"{n_idx} pairs of column indexes provided, "
                "but {n_schema} expected.")

    def _column_idx_checks(self, index_list):
        SchemaManager._type_check(index_list, list)
        self._assert_list_of_lists(index_list)
        self._assert_correct_len(index_list)
        self._assert_length_two(*index_list)
        self._assert_not_overlapping(index_list)
        self._assert_non_zero_width(index_list)
        flat_list = (item for sublist in index_list for item in sublist)
        self._assert_all_int(*flat_list)
        self._assert_all_positive(*flat_list)

    @property
    def column_idx(self):
        """List with index of column breaks."""
        idx = [[v["start"], v["end"]] for v in self.schema.values()]
        self._column_idx_checks(idx)
        return idx

    @column_idx.setter
    def column_idx(self, index_list):
        self._column_idx_checks(index_list)
        for i in range(len(index_list)):
            col = list(self.schema.keys())[i]
            self._schema[col]["start"] = index_list[i][0]
            self._schema[col]["end"] = index_list[i][1]
