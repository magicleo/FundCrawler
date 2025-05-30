"""
一些通用的正则表达式
"""
from enum import unique, StrEnum, Enum, auto

# 带千分号的 数字表达形式 -10,000.12
number_in_eng = r'-?(\d+?(,\d+)*?(\.\d+)?)'


@unique
class FundAttrKey(StrEnum):
    """
    基金属性枚举
    """
    FUND_CODE = '基金代码',
    FUND_SIMPLE_NAME = '基金简称',
    MORNINGSTAR_FUND_ID = '(晨星)基金代码',
    FUND_TYPE = '基金类型',
    FUND_CREATE_TIME = '基金发行日期',
    FUND_SIZE = '资产规模(亿)',
    MANAGEMENT_FEE_RATE = '管理费率(每年)',
    CUSTODY_FEE_RATE = '托管费率(每年)',
    SALES_SERVICE_FEE_RATE = '销售服务费率(每年)',

    FUND_COMPANY = '基金管理人',
    FUND_VALUE = '基金净值',
    # 兼容带新场景，A+B -> B -> B+C，此时基金经理为时长最长的B，对应的任职时间为 这三段 B连续任职的任职时间
    FUND_MANAGER = '基金经理(最近连续最长任职)',
    DATE_OF_APPOINTMENT = '基金经理的上任时间',


    ANNUALIZED_RETURN_ONE_MONTH = "一个月回报",
    ANNUALIZED_RETURN_THREE_MONTH = "三个月回报",
    ANNUALIZED_RETURN_SIX_MONTH = "六个月回报",
    ANNUALIZED_RETURN_THIS_YEAR = "今年以来回报",
    ANNUALIZED_RETURN_ONE_YEAR = "一年回报",
    ANNUALIZED_RETURN_TWO_YEAR = "二年回报（年化）",
    ANNUALIZED_RETURN_THREE_YEAR = "三年回报（年化）",
    ANNUALIZED_RETURN_FIVE_YEAR = "五年回报（年化）",
    ANNUALIZED_RETURN_TEN_YEAR = "十年回报（年化）",

    RETURN_ONE_YEAR = '回报(一年)'
    STANDARD_DEVIATION_ONE_YEAR = '标准差(一年)'
    MAXIMUM_DRAWDOWN_ONE_YEAR = '最大回撤(一年)'
    DOWNSIDE_RISK_ONE_YEAR = '下行风险(一年)'
    MORNINGSTAR_RISK_ONE_YEAR = '晨星风险(一年)'
    SHARPE_RATIO_ONE_YEAR = '夏普比例(一年)'
    CALMAR_RATIO_ONE_YEAR = '卡玛比率(一年)'
    SOTTINO_RATIO_ONE_YEAR= '索提诺比率(一年)'
    ALPHA_TO_IND_ONE_YEAR = '阿尔法系数(一年)',
    BETA_TO_IND_ONE_YEAR = '贝塔系数(一年)',
    R_SQUARED_TO_IND_ONE_YEAR = 'R平方(一年)',
    MONTHLY_WINNING_RATE_ONE_YEAR = '月度胜率(一年)'
    GROWTH_CAPTURE_RATE_ONE_YEAR = '涨势捕获率(一年)'
    BEARISH_CAPTURE_RATE_ONE_YEAR = '跌势捕获率(一年)'

    RETURN_THREE_YEAR = '回报(三年)'
    STANDARD_DEVIATION_THREE_YEAR = '标准差(三年)'
    MAXIMUM_DRAWDOWN_THREE_YEAR = '最大回撤(三年)'
    DOWNSIDE_RISK_THREE_YEAR = '下行风险(三年)'
    MORNINGSTAR_RISK_THREE_YEAR = '晨星风险(三年)'
    SHARPE_RATIO_THREE_YEAR = '夏普比例(三年)'
    CALMAR_RATIO_THREE_YEAR = '卡玛比率(三年)'
    SOTTINO_RATIO_THREE_YEAR= '索提诺比率(三年)'
    ALPHA_TO_IND_THREE_YEAR = '阿尔法系数(三年)',
    BETA_TO_IND_THREE_YEAR = '贝塔系数(三年)',
    R_SQUARED_TO_IND_THREE_YEAR = 'R平方(三年)',
    MONTHLY_WINNING_RATE_THREE_YEAR = '月度胜率(三年)'
    GROWTH_CAPTURE_RATE_THREE_YEAR = '涨势捕获率(三年)'
    BEARISH_CAPTURE_RATE_THREE_YEAR = '跌势捕获率(三年)'


    STANDARD_DEVIATION_THREE_YEARS = '标准差(三年%)',
    STANDARD_DEVIATION_FIVE_YEARS = '标准差(五年%)',
    STANDARD_DEVIATION_TEN_YEARS = '标准差(十年%)',
    SHARP_RATE_THREE_YEARS = '夏普比率(三年)',
    SHARP_RATE_FIVE_YEARS = '夏普比率(五年)',
    SHARP_RATE_TEN_YEARS = '夏普比率(十年)',
    ALPHA_TO_IND = '阿尔法系数(相对于基准指数%)',
    BETA_TO_IND = '贝塔系数(相对于基准指数)',
    R_SQUARED_TO_IND = 'R平方(相对于基准指数)',


@unique
class PageType(Enum):
    """
    页面的爬取和解析 枚举
    """
    # 基金概况 https://fundf10.eastmoney.com/jbgk_910009.html
    OVERVIEW = auto()
    # 基金经理 https://fundf10.eastmoney.com/jjjl_910009.html
    MANAGER = auto()
    # 晨星基本信息 https://www.morningstar.cn/handler/fundsearch.ashx?q=006922&limit=1
    MORNINGSTAR = auto()
    # 基金回报 https://www.morningstar.cn/handler/quicktake.ashx?command=return&fcid=0P00019IIB
    RETURN = auto()
    # 基金风险 https://www.morningstar.cn/handler/quicktake.ashx?command=rating&fcid=0P00019IIB
    RISK = auto()

    # 风险与回报https://www.morningstar.cn/#/fund/010430
    # https://www.morningstar.cn/cn-api/fund/risk-return-table?csdcc=010430&period=&flag=
    RISKRETURN = auto()

# 最终爬取结果文件的占位，用于区分是真的木有数据，还是爬取可能失败/遗漏
NO_DATA = 'NO_DATA'
DATA_ERROR = 'DATA_ERROR'
DATA_IGNORE = 'DATA_IGNORE'

# 日志输出格式
log_format = '%(asctime)s [%(processName)s/%(levelname)s] %(message)s'
