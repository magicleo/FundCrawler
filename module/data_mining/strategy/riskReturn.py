import json
from string import Template
from typing import Optional

from module.data_mining.strategy.data_mining_strategy import DataCleaningStrategy, NoNeedException
from module.downloader.download_by_requests import FundResponse
from module.fund_context import FundContext
from utils.constants import NO_DATA


class RiskReturnStrategy(DataCleaningStrategy):
    """
    基金的风险与回报指标，晨星页面中间风险tab
    https://www.morningstar.cn/#/fund/010430
    """

    url_template = Template(
        "https://www.morningstar.cn/cn-api/fund/risk-return-table?csdcc=$fund_code&period=&flag=")

    def build_url(self, context: FundContext) -> Optional[str]:
        return self.url_template.substitute(fund_code=context.fund_code)

    def fill_result(self, fund_response: FundResponse, context: FundContext) -> None:
        response = fund_response.response
        if response is None or not response.text  or response.text == 'null':
            context.return_one_year = NO_DATA
            context.standard_deviation_one_year = NO_DATA
            context.maximum_drawdown_one_year = NO_DATA
            context.downside_risk_one_year = NO_DATA
            context.morningstar_risk_one_year = NO_DATA
            context.sharp_ratio_one_year = NO_DATA
            context.calmar_ratio_one_year = NO_DATA
            context.sottino_ratio_one_year = NO_DATA
            context.alpha_to_ind_one_year = NO_DATA
            context.beta_to_ind_one_year = NO_DATA
            context.r_squared_to_ind_one_year = NO_DATA
            context.monthly_winning_rate_one_year = NO_DATA
            context.growth_capture_rate_one_year = NO_DATA
            context.bearish_capture_rate_one_year = NO_DATA

            context.return_three_year = NO_DATA
            context.standard_deviation_three_year = NO_DATA
            context.maximum_drawdown_three_year = NO_DATA
            context.downside_risk_three_year = NO_DATA
            context.morningstar_risk_three_year = NO_DATA
            context.sharp_ratio_three_year = NO_DATA
            context.calmar_ratio_three_year = NO_DATA
            context.sottino_ratio_three_year = NO_DATA
            context.alpha_to_ind_three_year = NO_DATA
            context.beta_to_ind_three_year = NO_DATA
            context.r_squared_to_ind_three_year = NO_DATA
            context.monthly_winning_rate_three_year = NO_DATA
            context.growth_capture_rate_three_year = NO_DATA
            context.bearish_capture_rate_three_year = NO_DATA

        return_json_list = json.loads(response.text)
        if not return_json_list.get('data',[]):
            return
        return_one = return_json_list['data'][0]
        if not return_one :
            return
        if return_one.get("0",[]):
            if return_one["0"][0].get("name", "") == "回报":
                context.return_one_year = return_one["0"][0]["value"] if return_one["0"][0]["value"] else NO_DATA
            if len(return_one["0"]) > 1 and return_one["0"][1].get("name","") == "标准差":
                context.standard_deviation_one_year = return_one["0"][1]["value"] if return_one["0"][1]["value"] else NO_DATA
        if return_one.get("1", []):
            if len(return_one["1"]) > 1 and  return_one["1"][1].get("name", "") == "最大回撤":
                context.maximum_drawdown_one_year = return_one["1"][1]["value"] if return_one["1"][1]["value"] else NO_DATA
            if len(return_one["1"]) > 2 and return_one["1"][2].get("name", "") == "下行风险":
                context.downside_risk_one_year = return_one["1"][2]["value"] if return_one["1"][2]["value"] else NO_DATA
            if len(return_one["1"]) > 3 and  return_one["1"][3].get("name", "") == "晨星风险":
                context.morningstar_risk_one_year = return_one["1"][3]["value"] if return_one["1"][3]["value"] else NO_DATA
        if return_one.get("2", []):
            if return_one["2"][0].get("name", "") == "夏普比率":
                context.sharp_ratio_one_year = return_one["2"][0]["value"] if return_one["2"][0]["value"] else NO_DATA
            if len(return_one["2"]) > 1 and  return_one["2"][1].get("name", "") == "卡玛比率":
                context.calmar_ratio_one_year = return_one["2"][1]["value"] if return_one["2"][1]["value"] else NO_DATA
            if len(return_one["2"]) > 2 and  return_one["2"][2].get("name", "") == "索提诺比率":
                context.sottino_ratio_one_year = return_one["2"][2]["value"] if return_one["2"][2]["value"] else NO_DATA

        if return_one.get("3", []):
            if return_one["3"][0].get("name", "") == "Alpha":
                context.alpha_to_ind_one_year = return_one["3"][0]["value"] if return_one["3"][0]["value"] else NO_DATA
            if  len(return_one["3"]) > 1 and  return_one["3"][1].get("name", "") == "Beta":
                context.beta_to_ind_one_year = return_one["3"][1]["value"] if return_one["3"][1]["value"] else NO_DATA
            if  len(return_one["3"]) > 2 and  return_one["3"][2].get("name", "") == "R2":
                context.r_squared_to_ind_one_year = return_one["3"][2]["value"] if return_one["3"][2]["value"] else NO_DATA
            if  len(return_one["3"]) > 3 and  return_one["3"][3].get("name", "") == "月度胜率":
                context.monthly_winning_rate_one_year = return_one["3"][3]["value"] if return_one["3"][3]["value"] else NO_DATA
            if  len(return_one["3"]) > 4 and  return_one["3"][4].get("name", "") == "涨势捕获率":
                context.growth_capture_rate_one_year = return_one["3"][4]["value"] if return_one["3"][4]["value"] else NO_DATA
            if  len(return_one["3"]) > 5 and  return_one["3"][5].get("name", "") == "跌势捕获率":
                context.growth_capture_rate_one_year = return_one["3"][5]["value"] if return_one["3"][5]["value"] else NO_DATA

        if len(return_json_list['data']) <= 1 :
            return
        return_three = return_json_list['data'][1]

        if not return_three :
            return
        if return_three.get("0",[]):
            if return_three["0"][0].get("name", "") == "回报":
                context.return_three_year = return_three["0"][0]["value"] if return_three["0"][0]["value"] else NO_DATA
            if len(return_three["0"]) > 1 and return_three["0"][1].get("name","") == "标准差":
                context.standard_deviation_three_year = return_three["0"][1]["value"] if return_three["0"][1]["value"] else NO_DATA
        if return_three.get("1", []):
            if len(return_three["1"]) > 1 and  return_three["1"][1].get("name", "") == "最大回撤":
                context.maximum_drawdown_three_year = return_three["1"][1]["value"] if return_three["1"][1]["value"] else NO_DATA
            if len(return_three["1"]) > 2 and return_three["1"][2].get("name", "") == "下行风险":
                context.downside_risk_three_year = return_three["1"][2]["value"] if return_three["1"][2]["value"] else NO_DATA
            if len(return_three["1"]) > 3 and  return_three["1"][3].get("name", "") == "晨星风险":
                context.morningstar_risk_three_year = return_three["1"][3]["value"] if return_three["1"][3]["value"] else NO_DATA
        if return_three.get("2", []):
            if return_three["2"][0].get("name", "") == "夏普比率":
                context.sharp_ratio_three_year = return_three["2"][0]["value"] if return_three["2"][0]["value"] else NO_DATA
            if len(return_three["2"]) > 1 and  return_three["2"][1].get("name", "") == "卡玛比率":
                context.calmar_ratio_three_year = return_three["2"][1]["value"] if return_three["2"][1]["value"] else NO_DATA
            if len(return_three["2"]) > 2 and  return_three["2"][2].get("name", "") == "索提诺比率":
                context.sottino_ratio_three_year = return_three["2"][2]["value"] if return_three["2"][2]["value"] else NO_DATA

        if return_three.get("3", []):
            if return_three["3"][0].get("name", "") == "Alpha":
                context.alpha_to_ind_three_year = return_three["3"][0]["value"] if return_three["3"][0]["value"] else NO_DATA
            if  len(return_three["3"]) > 1 and  return_three["3"][1].get("name", "") == "Beta":
                context.beta_to_ind_three_year = return_three["3"][1]["value"] if return_three["3"][1]["value"] else NO_DATA
            if  len(return_three["3"]) > 2 and  return_three["3"][2].get("name", "") == "R2":
                context.r_squared_to_ind_three_year = return_three["3"][2]["value"] if return_three["3"][2]["value"] else NO_DATA
            if  len(return_three["3"]) > 3 and  return_three["3"][3].get("name", "") == "月度胜率":
                context.monthly_winning_rate_three_year = return_three["3"][3]["value"] if return_three["3"][3]["value"] else NO_DATA
            if  len(return_three["3"]) > 4 and  return_three["3"][4].get("name", "") == "涨势捕获率":
                context.growth_capture_rate_three_year = return_three["3"][4]["value"] if return_three["3"][4]["value"] else NO_DATA
            if  len(return_three["3"]) > 5 and  return_three["3"][5].get("name", "") == "跌势捕获率":
                context.growth_capture_rate_three_year = return_three["3"][5]["value"] if return_three["3"][5]["value"] else NO_DATA



