from .common import SqlTableBase, SqlTableMixin
from sqlalchemy.orm import mapped_column
from sqlalchemy import String as SqlString, Boolean as SqlBool, Float as SqlFloat


class Branch(SqlTableBase, SqlTableMixin):
    """
    Read more: https://graphapi.cukcuk.vn/document/api/branchs_setting.html#branch-definition
    """

    __tablename__ = "branches"

    Id = mapped_column(SqlString(100), primary_key=True)
    Code = mapped_column(SqlString)
    Name = mapped_column(SqlString)
    IsBaseDepot = mapped_column(SqlBool)
    IsChainBranch = mapped_column(SqlBool)
    HasVATRate = mapped_column(SqlBool)
    VATForDelivery = mapped_column(SqlBool)
    VATForTakeAway = mapped_column(SqlBool)
    VATForShip = mapped_column(SqlBool)
    VATRate = mapped_column(SqlFloat)
    HasCalcService = mapped_column(SqlBool)
    CalcServiceDelivery = mapped_column(SqlBool)
    CalcServiceTakeAway = mapped_column(SqlBool)
    IsCalcServiceAmountNotPromotion = mapped_column(SqlBool)
    CalTaxForService = mapped_column(SqlBool)
    HasServiceRate = mapped_column(SqlBool)
    ServiceRate = mapped_column(SqlFloat)
    HasAmountService = mapped_column(SqlBool)
    AmountService = mapped_column(SqlFloat)
