from abc import ABC, abstractmethod

class AbstractMethod(ABC):
    """
    abstract class which defines a basic data structure
    for a method filled with the default values
    """
    def __init__(self):

        # define a common data structure
        self.method_data = {'cs': None,
                            'ynxtLstStg': None,
                            'errInGo': None,
                            'takeErrStage': None,
                            'useimplf0': None,
                            'itercount': None,
                            't_Dinput_exact': None,
                            'T': None,
                            'Tinv': None,
                            'Lamb': None,
                            'Alph_singl_sum': None,
                            'Gam_singl_sum': None,
                            'calA': None,
                            'Alpha_subA_TI': None,
                            'Alp0_m_Alph_subA_a0': None,
                            'neg_invD_Gamm_subA_TI': None,
                            'invD_Gamm_subA_a0': None,
                            'invDprod': None,
                            'b_invA_TI': None,
                            'Tinv_Ab': None,
                            'Blocktype': "kxk",
                            'bsize': None,
                            'ssize': None,
                            'a0': None,
                            'b_invA_a0mb0': None,
                            'Tinv_invA_a0': None,
                            'b0': None,
                            'expl_meth': None,
                            'expl1stg': None,
                            'bs': None,
                            'interpol_weights': None,
                            'pureWmeth': None,
                            'extWmeth': None,
                            'locerr_pot': None,
                            'norm_bsadd_Ainv': None,
                            'bsadd_invA_TI': None,
                            'poldeg': None,
                            'tryT2': None,
                            'abl_r': None,
                            'order': None}

        self.adjust_data_structure()


    @abstractmethod
    def adjust_data_structure(self):
        pass


    def get_data(self):
        return self.method_data