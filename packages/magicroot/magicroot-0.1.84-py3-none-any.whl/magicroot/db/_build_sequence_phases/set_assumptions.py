from ..tables import *


class AssumptionsTable(BuildSequenceProperties):

    def _phase_set_assumptions(self, *args, **kwargs):
        # df = self.set_assumptions(self._created_table, *args, **kwargs)
        df = self.set_assumptions(self.create_module.output, *args, **kwargs)
        self._assumptions_table = df
        return {'set_assumption_result': df}

