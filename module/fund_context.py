"""
模块间交互所使用的BO
"""
from typing import Optional

from module.downloader.download_by_requests import FundResponse
from utils.constants import FundAttrKey, PageType


class FundContext:
    """
    基金爬取数据的上下文
    """

    def __init__(self, fund_code: str, fund_name: str):
        self.fund_code: str = fund_code
        self.fund_name: str = fund_name
        # 晨星的基金标识
        self.morningstar_fund_id: Optional[str] = None
        self.fund_type: Optional[str] = None
        self.fund_create_time: Optional[str] = None
        self.fund_size: Optional[str] = None
        self.fund_company: Optional[str] = None
        self.fund_value: Optional[str] = None
        self.fund_manager: Optional[str] = None
        self.date_of_appointment: Optional[str] = None
        self.management_fee_rate: Optional[str] = None
        self.custody_fee_rate: Optional[str] = None
        self.sales_service_fee_rate: Optional[str] = None
        self.annualized_return_one_month: Optional[str] = None
        self.annualized_return_three_month: Optional[str] = None
        self.annualized_return_six_month: Optional[str] = None
        self.annualized_return_this_year: Optional[str] = None
        self.annualized_return_one_year: Optional[str] = None
        self.annualized_return_two_year: Optional[str] = None
        self.annualized_return_three_year: Optional[str] = None
        self.annualized_return_five_year: Optional[str] = None
        self.annualized_return_ten_year: Optional[str] = None
        self.return_one_year: Optional[str] = None
        self.standard_deviation_one_year: Optional[str] = None
        self.maximum_drawdown_one_year: Optional[str] = None
        self.downside_risk_one_year: Optional[str] = None
        self.morningstar_risk_one_year: Optional[str] = None
        self.sharp_ratio_one_year: Optional[str] = None
        self.calmar_ratio_one_year: Optional[str] = None
        self.sottino_ratio_one_year: Optional[str] = None
        self.alpha_to_ind_one_year: Optional[str] = None
        self.beta_to_ind_one_year: Optional[str] = None
        self.r_squared_to_ind_one_year: Optional[str] = None
        self.monthly_winning_rate_one_year: Optional[str] = None
        self.growth_capture_rate_one_year: Optional[str] = None
        self.bearish_capture_rate_one_year: Optional[str] = None

        self.return_three_year: Optional[str] = None
        self.standard_deviation_three_year: Optional[str] = None
        self.maximum_drawdown_three_year: Optional[str] = None
        self.downside_risk_three_year: Optional[str] = None
        self.morningstar_risk_three_year: Optional[str] = None
        self.sharp_ratio_three_year: Optional[str] = None
        self.calmar_ratio_three_year: Optional[str] = None
        self.sottino_ratio_three_year: Optional[str] = None
        self.alpha_to_ind_three_year: Optional[str] = None
        self.beta_to_ind_three_year: Optional[str] = None
        self.r_squared_to_ind_three_year: Optional[str] = None
        self.monthly_winning_rate_three_year: Optional[str] = None
        self.growth_capture_rate_three_year: Optional[str] = None
        self.bearish_capture_rate_three_year: Optional[str] = None

        self.standard_deviation_three_years: Optional[str] = None
        self.standard_deviation_five_years: Optional[str] = None
        self.standard_deviation_ten_years: Optional[str] = None
        self.sharp_rate_three_years: Optional[str] = None
        self.sharp_rate_five_years: Optional[str] = None
        self.sharp_rate_ten_years: Optional[str] = None
        self.alpha_to_ind: Optional[str] = None
        self.beta_to_ind: Optional[str] = None
        self.r_squared_to_ind: Optional[str] = None

        # 爬取到的网页数据
        self.http_response_dict: dict[PageType, FundResponse] = dict()

    def to_result_row(self) -> dict[FundAttrKey, Optional[str]]:
        return {
            FundAttrKey.FUND_CODE: self.fund_code,
            FundAttrKey.FUND_SIMPLE_NAME: self.fund_name,
            FundAttrKey.MORNINGSTAR_FUND_ID: self.morningstar_fund_id,
            FundAttrKey.FUND_TYPE: self.fund_type,
            FundAttrKey.FUND_CREATE_TIME: self.fund_create_time,
            FundAttrKey.FUND_SIZE: self.fund_size,
            FundAttrKey.FUND_COMPANY: self.fund_company,
            FundAttrKey.FUND_VALUE: self.fund_value,
            FundAttrKey.FUND_MANAGER: self.fund_manager,
            FundAttrKey.DATE_OF_APPOINTMENT: self.date_of_appointment,
            FundAttrKey.MANAGEMENT_FEE_RATE: self.management_fee_rate,
            FundAttrKey.CUSTODY_FEE_RATE: self.custody_fee_rate,
            FundAttrKey.SALES_SERVICE_FEE_RATE: self.sales_service_fee_rate,
            FundAttrKey.ANNUALIZED_RETURN_ONE_MONTH: self.annualized_return_one_month,
            FundAttrKey.ANNUALIZED_RETURN_THREE_MONTH: self.annualized_return_three_month,
            FundAttrKey.ANNUALIZED_RETURN_SIX_MONTH: self.annualized_return_six_month,
            FundAttrKey.ANNUALIZED_RETURN_THIS_YEAR: self.annualized_return_this_year,
            FundAttrKey.ANNUALIZED_RETURN_ONE_YEAR: self.annualized_return_one_year,
            FundAttrKey.ANNUALIZED_RETURN_TWO_YEAR: self.annualized_return_two_year,
            FundAttrKey.ANNUALIZED_RETURN_THREE_YEAR: self.annualized_return_three_year,
            FundAttrKey.ANNUALIZED_RETURN_FIVE_YEAR: self.annualized_return_five_year,
            FundAttrKey.ANNUALIZED_RETURN_TEN_YEAR: self.annualized_return_ten_year,

            FundAttrKey.RETURN_ONE_YEAR: self.return_one_year,
            FundAttrKey.STANDARD_DEVIATION_ONE_YEAR: self.standard_deviation_one_year,
            FundAttrKey.MAXIMUM_DRAWDOWN_ONE_YEAR: self.maximum_drawdown_one_year,
            FundAttrKey.DOWNSIDE_RISK_ONE_YEAR: self.downside_risk_one_year,
            FundAttrKey.MORNINGSTAR_RISK_ONE_YEAR: self.morningstar_risk_one_year,
            FundAttrKey.SHARPE_RATIO_ONE_YEAR: self.sharp_ratio_one_year,

            FundAttrKey.CALMAR_RATIO_ONE_YEAR: self.calmar_ratio_one_year,
            FundAttrKey.SOTTINO_RATIO_ONE_YEAR: self.sottino_ratio_one_year,
            FundAttrKey.ALPHA_TO_IND_ONE_YEAR: self.alpha_to_ind_one_year,
            FundAttrKey.BETA_TO_IND_ONE_YEAR: self.beta_to_ind_one_year,
            FundAttrKey.R_SQUARED_TO_IND_ONE_YEAR: self.r_squared_to_ind_one_year,

            FundAttrKey.MONTHLY_WINNING_RATE_ONE_YEAR: self.monthly_winning_rate_one_year,
            FundAttrKey.GROWTH_CAPTURE_RATE_ONE_YEAR: self.growth_capture_rate_one_year,
            FundAttrKey.BEARISH_CAPTURE_RATE_ONE_YEAR: self.bearish_capture_rate_one_year,

            FundAttrKey.RETURN_THREE_YEAR: self.return_three_year,
            FundAttrKey.STANDARD_DEVIATION_THREE_YEAR: self.standard_deviation_three_year,
            FundAttrKey.MAXIMUM_DRAWDOWN_THREE_YEAR: self.maximum_drawdown_three_year,
            FundAttrKey.DOWNSIDE_RISK_THREE_YEAR: self.downside_risk_three_year,
            FundAttrKey.MORNINGSTAR_RISK_THREE_YEAR: self.morningstar_risk_three_year,
            FundAttrKey.SHARPE_RATIO_THREE_YEAR: self.sharp_ratio_three_year,
            FundAttrKey.CALMAR_RATIO_THREE_YEAR: self.calmar_ratio_three_year,
            FundAttrKey.SOTTINO_RATIO_THREE_YEAR: self.sottino_ratio_three_year,
            FundAttrKey.ALPHA_TO_IND_THREE_YEAR: self.alpha_to_ind_three_year,
            FundAttrKey.BETA_TO_IND_THREE_YEAR: self.beta_to_ind_three_year,
            FundAttrKey.R_SQUARED_TO_IND_THREE_YEAR: self.r_squared_to_ind_three_year,
            FundAttrKey.MONTHLY_WINNING_RATE_THREE_YEAR: self.monthly_winning_rate_three_year,
            FundAttrKey.GROWTH_CAPTURE_RATE_THREE_YEAR: self.growth_capture_rate_three_year,
            FundAttrKey.BEARISH_CAPTURE_RATE_THREE_YEAR: self.bearish_capture_rate_three_year,

            FundAttrKey.STANDARD_DEVIATION_THREE_YEARS: self.standard_deviation_three_years,
            FundAttrKey.STANDARD_DEVIATION_FIVE_YEARS: self.standard_deviation_five_years,
            FundAttrKey.STANDARD_DEVIATION_TEN_YEARS: self.standard_deviation_ten_years,
            FundAttrKey.SHARP_RATE_THREE_YEARS: self.sharp_rate_three_years,
            FundAttrKey.SHARP_RATE_FIVE_YEARS: self.sharp_rate_five_years,
            FundAttrKey.SHARP_RATE_TEN_YEARS: self.sharp_rate_ten_years,
            FundAttrKey.ALPHA_TO_IND: self.alpha_to_ind,
            FundAttrKey.BETA_TO_IND: self.beta_to_ind,
            FundAttrKey.R_SQUARED_TO_IND: self.r_squared_to_ind,
        }
