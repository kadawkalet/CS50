from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify
from flask_session import Session
from tempfile import mkdtemp


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.template_filter()
def usd(value):
    value = float(value)
    return "${:,.2f}".format(value)

@app.template_filter()
def two_dec(value):
    value = float(value)
    return "{:,.2f}".format(value)

@app.route('/home')
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/activity_ratios", methods=["GET", "POST"])
def activity_ratios():
    return render_template("activity_ratios.html")

@app.route("/basic_equations", methods=["GET", "POST"])
def basic_equations():
    return render_template("basic_equations.html")

@app.route("/debt_ratios", methods=["GET", "POST"])
def debt_ratios():
    return render_template("debt_ratios.html")

@app.route("/depreciation", methods=["GET", "POST"])
def depreciation():
    return render_template("depreciation.html")

@app.route("/liquidity_ratios", methods=["GET", "POST"])
def liquidity_ratios():
    return render_template("liquidity_ratios.html")

@app.route("/market_ratios", methods=["GET", "POST"])
def market_ratios():
    return render_template("market_ratios.html")

@app.route("/profitability_ratios", methods=["GET", "POST"])
def profitability_ratios():
    return render_template("profitability_ratios.html")

@app.route("/asset_turnover", methods=["GET", "POST"])
def asset_turnover():
    if request.method == "POST":

        if not request.form.get("net_asset") or not request.form.get("total_asset"):
            x = 1
            return render_template("asset_turnover.html", x=x)
        
        net_asset = float(request.form.get("net_asset"))
        total_asset = float(request.form.get("total_asset"))

        ratio = net_asset / total_asset

        return render_template("asset_turnover.html", ratio=ratio, net_asset=net_asset, total_asset=total_asset)
    else:
        return render_template("asset_turnover.html")

@app.route("/avg_collection", methods=["GET", "POST"])
def avg_collection():
    if request.method == "POST":

        if not request.form.get("account_receivables") or not request.form.get("annual_credit_sales"):
            x = 1
            return render_template("avg_collection.html", x=x)

        account_receivables = float(request.form.get("account_receivables"))
        annual_credit_sales = float(request.form.get("annual_credit_sales"))

        ratio = account_receivables / (annual_credit_sales / 365)

        return render_template("avg_collection.html", ratio=ratio, account_receivables=account_receivables, annual_credit_sales=annual_credit_sales)
    else:
        return render_template("avg_collection.html")

@app.route("/cash_conversion", methods=["GET", "POST"])
def cash_conversion():
    if request.method == "POST":

        if not request.form.get("inventory_conversion") or not request.form.get("receivables_conversion") or not request.form.get("payables_conversion"):
            x = 1
            return render_template("cash_conversion.html", x=x)

        inventory_conversion = float(request.form.get("inventory_conversion"))
        receivables_conversion = float(request.form.get("receivables_conversion"))
        payables_conversion = float(request.form.get("payables_conversion"))

        ratio = inventory_conversion + receivables_conversion - payables_conversion

        return render_template("cash_conversion.html", ratio=ratio, inventory_conversion=inventory_conversion, receivables_conversion=receivables_conversion, payables_conversion=payables_conversion)
    else:
        return render_template("cash_conversion.html")

@app.route("/inventory_conversion_period", methods=["GET", "POST"])
def inventory_conversion_period():
    if request.method == "POST":

        if not request.form.get("inventory") or not request.form.get("cogs"):
            x = 1
            return render_template("inventory_conversion_period.html", x=x)

        inventory = float(request.form.get("inventory"))
        cogs = float(request.form.get("cogs"))

        ratio = (inventory / cogs) * 365

        return render_template("inventory_conversion_period.html", ratio=ratio, inventory=inventory, cogs=cogs)
    else:
        return render_template("inventory_conversion_period.html")

@app.route("/inventory_conversion", methods=["GET", "POST"])
def inventory_conversion():
    if request.method == "POST":

        if not request.form.get("sales") or not request.form.get("cogs"):
            x = 1
            return render_template("inventory_conversion.html", x=x)

        sales = float(request.form.get("sales"))
        cogs = float(request.form.get("cogs"))

        ratio = (sales * 0.5) / cogs

        return render_template("inventory_conversion.html", ratio=ratio, sales=sales, cogs=cogs)
    else:
        return render_template("inventory_conversion.html")

@app.route("/it", methods=["GET", "POST"])
def it():
    if request.method == "POST":

        if not request.form.get("sales") or not request.form.get("avg_inventory"):
            x = 1
            return render_template("it.html", x=x)

        sales = float(request.form.get("sales"))
        avg_inventory = float(request.form.get("avg_inventory"))

        ratio = sales / avg_inventory

        return render_template("it.html", ratio=ratio, sales=sales, avg_inventory=avg_inventory)
    else:
        return render_template("it.html")

@app.route("/pcp", methods=["GET", "POST"])
def pcp():
    if request.method == "POST":

        if not request.form.get("acc_payable") or not request.form.get("purchases"):
            x = 1
            return render_template("pcp.html", x=x)

        acc_payable = float(request.form.get("acc_payable"))
        purchases = float(request.form.get("purchases"))

        ratio = (acc_payable / purchases) * 365 

        return render_template("pcp.html", ratio=ratio, acc_payable=acc_payable, purchases=purchases)
    else:
        return render_template("pcp.html")

@app.route("/rcp", methods=["GET", "POST"])
def rcp():
    if request.method == "POST":

        if not request.form.get("acc_receivable") or not request.form.get("net_sales"):
            x = 1
            return render_template("rcp.html", x=x)

        acc_receivable = float(request.form.get("acc_receivable"))
        net_sales = float(request.form.get("net_sales"))

        ratio = (acc_receivable / net_sales) * 365 

        return render_template("rcp.html", ratio=ratio, acc_receivable=acc_receivable, net_sales=net_sales)
    else:
        return render_template("rcp.html")

@app.route("/rtr", methods=["GET", "POST"])
def rtr():
    if request.method == "POST":

        if not request.form.get("ncs") or not request.form.get("anr"):
            x = 1
            return render_template("rtr.html", x=x)

        ncs = float(request.form.get("ncs"))
        anr = float(request.form.get("anr"))

        ratio = ncs / anr

        return render_template("rtr.html", ratio=ratio, ncs=ncs, anr=anr)
    else:
        return render_template("rtr.html")

@app.route("/asset", methods=["GET", "POST"])
def asset():
    if request.method == "POST":

        if not request.form.get("liabilities") or not request.form.get("equity"):
            x = 1
            return render_template("basic_equations.html", x=x)

        liabilities = float(request.form.get("liabilities"))
        equity = float(request.form.get("equity"))

        ratio = liabilities + equity

        return render_template("basic_equations.html", ratio=ratio)
    else:
        return render_template("basic_equations.html")

@app.route("/ebit", methods=["GET", "POST"])
def ebit():
    if request.method == "POST":

        if not request.form.get("revenue") or not request.form.get("oe"):
            x = 1
            return render_template("basic_equations.html", x=x)

        revenue = float(request.form.get("revenue"))
        oe = float(request.form.get("oe"))

        ratio = revenue - oe

        return render_template("basic_equations.html", ratio=ratio)
    else:
        return render_template("basic_equations.html")

@app.route("/equity", methods=["GET", "POST"])
def equity():
    if request.method == "POST":

        if not request.form.get("asset") or not request.form.get("liability"):
            x = 1
            return render_template("basic_equations.html", x=x)

        asset = float(request.form.get("asset"))
        liability = float(request.form.get("liability"))

        ratio = asset - liability

        return render_template("basic_equations.html", ratio=ratio)
    else:
        return render_template("basic_equations.html")

@app.route("/gross_profit", methods=["GET", "POST"])
def gross_profit():
    if request.method == "POST":

        if not request.form.get("revenue") or not request.form.get("cogs"):
            x = 1
            return render_template("basic_equations.html", x=x)

        revenue = float(request.form.get("revenue"))
        cogs = float(request.form.get("cogs"))

        ratio = revenue - cogs

        return render_template("basic_equations.html", ratio=ratio)
    else:
        return render_template("basic_equations.html")

@app.route("/liability", methods=["GET", "POST"])
def liability():
    if request.method == "POST":

        if not request.form.get("asset") or not request.form.get("equity"):
            x = 1
            return render_template("basic_equations.html", x=x)

        asset = float(request.form.get("asset"))
        equity = float(request.form.get("equity"))

        ratio = asset - equity

        return render_template("basic_equations.html", ratio=ratio)
    else:
        return render_template("basic_equations.html")

@app.route("/net_profit", methods=["GET", "POST"])
def net_profit():
    if request.method == "POST":

        if not request.form.get("gross_profit") or not request.form.get("oe") or not request.form.get("taxes") or not request.form.get("interest"):
            x = 1
            return render_template("basic_equations.html", x=x)

        gross_profit = float(request.form.get("gross_profit"))
        oe = float(request.form.get("oe"))
        taxes = float(request.form.get("taxes"))
        interest = float(request.form.get("interest"))

        ratio = gross_profit - oe - taxes - interest

        return render_template("basic_equations.html", ratio=ratio)
    else:
        return render_template("basic_equations.html")

@app.route("/operating_profit", methods=["GET", "POST"])
def operating_profit():
    if request.method == "POST":

        if not request.form.get("gross_profit") or not request.form.get("operating_expenses"):
            x = 1
            return render_template("basic_equations.html", x=x)

        gross_profit = float(request.form.get("gross_profit"))
        operating_expenses = float(request.form.get("operating_expenses"))

        ratio = gross_profit - operating_expenses

        return render_template("basic_equations.html", ratio=ratio)
    else:
        return render_template("basic_equations.html")

@app.route("/sales", methods=["GET", "POST"])
def sales():
    if request.method == "POST":

        if not request.form.get("gross_sales") or not request.form.get("return_allowances"):
            x = 1
            return render_template("basic_equations.html", x=x)

        gross_sales = float(request.form.get("gross_sales"))
        return_allowances = float(request.form.get("return_allowances"))

        ratio = gross_sales - return_allowances

        return render_template("basic_equations.html", ratio=ratio)
    else:
        return render_template("basic_equations.html")

@app.route("/d_t_e", methods=["GET", "POST"])
def d_t_e():
    if request.method == "POST":

        if not request.form.get("liability") or not request.form.get("equity"):
            x = 1
            return render_template("debt_ratios.html", x=x)

        liability = float(request.form.get("liability"))
        equity = float(request.form.get("equity"))

        ratio = liability / equity

        return render_template("debt_ratios.html", ratio=ratio)
    else:
        return render_template("debt_ratios.html")

@app.route("/debt_ratio", methods=["GET", "POST"])
def debt_ratio():
    if request.method == "POST":

        if not request.form.get("liability") or not request.form.get("asset"):
            x = 1
            return render_template("debt_ratios.html", x=x)

        liability = float(request.form.get("liability"))
        asset = float(request.form.get("asset"))

        ratio = liability / asset

        return render_template("debt_ratios.html", ratio=ratio)
    else:
        return render_template("debt_ratios.html")

@app.route("/d_s_c_r", methods=["GET", "POST"])
def d_s_c_r():
    if request.method == "POST":

        if not request.form.get("noi") or not request.form.get("tds"):
            x = 1
            return render_template("debt_ratios.html", x=x)

        noi = float(request.form.get("noi"))
        tds = float(request.form.get("tds"))

        ratio = noi / tds

        return render_template("debt_ratios.html", ratio=ratio)
    else:
        return render_template("debt_ratios.html")

@app.route("/l_t_d_e_r", methods=["GET", "POST"])
def l_t_d_e_r():
    if request.method == "POST":

        if not request.form.get("l_t_l") or not request.form.get("l_t_l"):
            x = 1
            return render_template("debt_ratios.html", x=x)

        l_t_l = float(request.form.get("l_t_l"))
        equity = float(request.form.get("equity"))

        ratio = l_t_l / equity

        return render_template("debt_ratios.html", ratio=ratio)
    else:
        return render_template("debt_ratios.html")

@app.route("/book_value", methods=["GET", "POST"])
def book_value():
    if request.method == "POST":

        if not request.form.get("ac") or not request.form.get("depreciation"):
            x = 1
            return render_template("depreciation.html", x=x)

        ac = float(request.form.get("ac"))
        depreciation = float(request.form.get("depreciation"))

        ratio = ac - depreciation

        return render_template("depreciation.html", ratio=ratio)
    else:
        return render_template("depreciation.html")

@app.route("/declining_balance", methods=["GET", "POST"])
def declining_balance():
    if request.method == "POST":

        if not request.form.get("dr") or not request.form.get("book_value"):
            x = 1
            return render_template("depreciation.html", x=x)

        dr = float(request.form.get("dr"))
        book_value = float(request.form.get("book_value"))

        ratio = dr * book_value

        return render_template("depreciation.html", ratio=ratio)
    else:
        return render_template("depreciation.html")

@app.route("/sl_method", methods=["GET", "POST"])
def sl_method():
    if request.method == "POST":

        if not request.form.get("coa") or not request.form.get("rv") or not request.form.get("ula"):
            x = 1
            return render_template("depreciation.html", x=x)

        coa = float(request.form.get("coa"))
        rv = float(request.form.get("rv"))
        ula = float(request.form.get("ula"))

        ratio = (coa - rv) / ula

        return render_template("depreciation.html", ratio=ratio)
    else:
        return render_template("depreciation.html")

@app.route("/uo_prod", methods=["GET", "POST"])
def uo_prod():
    if request.method == "POST":

        if not request.form.get("coa") or not request.form.get("rv") or not request.form.get("etp") or not request.form.get("ap"):
            x = 1
            return render_template("depreciation.html", x=x)

        coa = float(request.form.get("coa"))
        rv = float(request.form.get("rv"))
        etp = float(request.form.get("etp"))
        ap = float(request.form.get("ap"))

        ratio = ((coa - rv) / etp) * ap

        return render_template("depreciation.html", ratio=ratio)
    else:
        return render_template("depreciation.html")

@app.route("/quick_ratio", methods=["GET", "POST"])
def quick_ratio():
    if request.method == "POST":

        if not request.form.get("ca") or not request.form.get("inventory") or not request.form.get("cl"):
            x = 1
            return render_template("liquidity_ratios.html", x=x)

        ca = float(request.form.get("ca"))
        inventory = float(request.form.get("inventory"))
        cl = float(request.form.get("cl"))

        ratio = (ca - inventory) / cl

        return render_template("liquidity_ratios.html", ratio=ratio)
    else:
        return render_template("liquidity_ratios.html")

@app.route("/cash_ratio", methods=["GET", "POST"])
def cash_ratio():
    if request.method == "POST":

        if not request.form.get("cash") or not request.form.get("ms") or not request.form.get("cl"):
            x = 1
            return render_template("liquidity_ratios.html", x=x)

        cash = float(request.form.get("cash"))
        ms = float(request.form.get("ms"))
        cl = float(request.form.get("cl"))

        ratio = (cash + ms) / cl

        return render_template("liquidity_ratios.html", ratio=ratio)
    else:
        return render_template("liquidity_ratios.html")

@app.route("/current_ratio", methods=["GET", "POST"])
def current_ratio():
    if request.method == "POST":

        if not request.form.get("ca") or not request.form.get("cl"):
            x = 1
            return render_template("liquidity_ratios.html", x=x)

        ca = float(request.form.get("ca"))
        cl = float(request.form.get("cl"))

        ratio = ca / cl

        return render_template("liquidity_ratios.html", ratio=ratio)
    else:
        return render_template("liquidity_ratios.html")

@app.route("/ocf_ratio", methods=["GET", "POST"])
def ocf_ratio():
    if request.method == "POST":

        if not request.form.get("ocf") or not request.form.get("td"):
            x = 1
            return render_template("liquidity_ratios.html", x=x)

        ocf = float(request.form.get("ocf"))
        td = float(request.form.get("td"))

        ratio = ocf / td

        return render_template("liquidity_ratios.html", ratio=ratio)
    else:
        return render_template("liquidity_ratios.html")

@app.route("/div_cover", methods=["GET", "POST"])
def div_cover():
    if request.method == "POST":

        if not request.form.get("eps") or not request.form.get("dps"):
            x = 1
            return render_template("market_ratios.html", x=x)

        eps = float(request.form.get("eps"))
        dps = float(request.form.get("dps"))

        ratio = eps / dps

        return render_template("market_ratios.html", ratio=ratio)
    else:
        return render_template("market_ratios.html")

@app.route("/div_yield", methods=["GET", "POST"])
def div_yield():
    if request.method == "POST":

        if not request.form.get("dps") or not request.form.get("sp"):
            x = 1
            return render_template("market_ratios.html", x=x)

        dps = float(request.form.get("dps"))
        sp = float(request.form.get("sp"))

        ratio = dps / sp

        return render_template("market_ratios.html", ratio=ratio)
    else:
        return render_template("market_ratios.html")

@app.route("/dps", methods=["GET", "POST"])
def dps():
    if request.method == "POST":

        if not request.form.get("div") or not request.form.get("shares"):
            x = 1
            return render_template("market_ratios.html", x=x)

        div = float(request.form.get("div"))
        shares = float(request.form.get("shares"))

        ratio = div / shares

        return render_template("market_ratios.html", ratio=ratio)
    else:
        return render_template("market_ratios.html")

@app.route("/eps", methods=["GET", "POST"])
def eps():
    if request.method == "POST":

        if not request.form.get("earnings") or not request.form.get("shares"):
            x = 1
            return render_template("market_ratios.html", x=x)

        earnings = float(request.form.get("earnings"))
        shares = float(request.form.get("shares"))

        ratio = earnings / shares

        return render_template("market_ratios.html", ratio=ratio)
    else:
        return render_template("market_ratios.html")

@app.route("/payout_ratio", methods=["GET", "POST"])
def payout_ratio():
    if request.method == "POST":

        if not request.form.get("div") or not request.form.get("earnings"):
            x = 1
            return render_template("market_ratios.html", x=x)

        div = float(request.form.get("div"))
        earnings = float(request.form.get("earnings"))

        ratio = div / earnings

        return render_template("market_ratios.html", ratio=ratio)
    else:
        return render_template("market_ratios.html")

@app.route("/peg_ratio", methods=["GET", "POST"])
def peg_ratio():
    if request.method == "POST":

        if not request.form.get("sp") or not request.form.get("eps") or not request.form.get("eps_growth"):
            x = 1
            return render_template("market_ratios.html", x=x)

        sp = float(request.form.get("sp"))
        eps = float(request.form.get("eps"))
        eps_growth = float(request.form.get("eps_growth"))

        ratio = (sp / eps) / eps_growth

        return render_template("market_ratios.html", ratio=ratio)
    else:
        return render_template("market_ratios.html")

@app.route("/p_s", methods=["GET", "POST"])
def p_s():
    if request.method == "POST":

        if not request.form.get("sp") or not request.form.get("sales") or not request.form.get("shares"):
            x = 1
            return render_template("market_ratios.html", x=x)

        sp = float(request.form.get("sp"))
        sales = float(request.form.get("sales"))
        shares = float(request.form.get("shares"))

        ratio = sp / (sales / shares)

        return render_template("market_ratios.html", ratio=ratio)
    else:
        return render_template("market_ratios.html")

@app.route("/eff_ratio", methods=["GET", "POST"])
def eff_ratio():
    if request.method == "POST":

        if not request.form.get("nie") or not request.form.get("sales"):
            x = 1
            return render_template("profitability_ratios.html", x=x)

        nie = float(request.form.get("nie"))
        sales = float(request.form.get("sales"))

        ratio = nie / sales

        return render_template("profitability_ratios.html", ratio=ratio)
    else:
        return render_template("profitability_ratios.html")

@app.route("/gp_ratio", methods=["GET", "POST"])
def gp_ratio():
    if request.method == "POST":

        if not request.form.get("gp") or not request.form.get("sales"):
            x = 1
            return render_template("profitability_ratios.html", x=x)

        gp = float(request.form.get("gp"))
        sales = float(request.form.get("sales"))

        ratio = gp / sales

        return render_template("profitability_ratios.html", ratio=ratio)
    else:
        return render_template("profitability_ratios.html")

@app.route("/r_s", methods=["GET", "POST"])
def r_s():
    if request.method == "POST":

        if not request.form.get("oi") or not request.form.get("sales"):
            x = 1
            return render_template("profitability_ratios.html", x=x)

        oi = float(request.form.get("oi"))
        sales = float(request.form.get("sales"))

        ratio = oi / sales

        return render_template("profitability_ratios.html", ratio=ratio)
    else:
        return render_template("profitability_ratios.html")

@app.route("/np_ratio", methods=["GET", "POST"])
def np_ratio():
    if request.method == "POST":

        if not request.form.get("np") or not request.form.get("sales"):
            x = 1
            return render_template("profitability_ratios.html", x=x)

        np = float(request.form.get("np"))
        sales = float(request.form.get("sales"))

        ratio = np / sales

        return render_template("profitability_ratios.html", ratio=ratio)
    else:
        return render_template("profitability_ratios.html")

@app.route("/r_a", methods=["GET", "POST"])
def r_a():
    if request.method == "POST":

        if not request.form.get("ni") or not request.form.get("asset"):
            x = 1
            return render_template("profitability_ratios.html", x=x)

        ni = float(request.form.get("ni"))
        asset = float(request.form.get("asset"))

        ratio = ni / asset

        return render_template("profitability_ratios.html", ratio=ratio)
    else:
        return render_template("profitability_ratios.html")

@app.route("/r_c", methods=["GET", "POST"])
def r_c():
    if request.method == "POST":

        if not request.form.get("ebit") or not request.form.get("rate") or not request.form.get("capital"):
            x = 1
            return render_template("profitability_ratios.html", x=x)

        ebit = float(request.form.get("ebit"))
        rate = float(request.form.get("rate"))
        capital = float(request.form.get("capital"))

        ratio = (ebit * (1 - rate)) / capital

        return render_template("profitability_ratios.html", ratio=ratio)
    else:
        return render_template("profitability_ratios.html")

@app.route("/r_e", methods=["GET", "POST"])
def r_e():
    if request.method == "POST":

        if not request.form.get("ni") or not request.form.get("equity"):
            x = 1
            return render_template("profitability_ratios.html", x=x)

        ni = float(request.form.get("ni"))
        equity = float(request.form.get("equity"))

        ratio = ni / equity

        return render_template("profitability_ratios.html", ratio=ratio)
    else:
        return render_template("profitability_ratios.html")

@app.route("/r_i", methods=["GET", "POST"])
def r_i():
    if request.method == "POST":

        if not request.form.get("gain") or not request.form.get("cost"):
            x = 1
            return render_template("profitability_ratios.html", x=x)

        gain = float(request.form.get("gain"))
        cost = float(request.form.get("cost"))

        ratio = (gain - cost) / cost

        return render_template("profitability_ratios.html", ratio=ratio)
    else:
        return render_template("profitability_ratios.html")

@app.route("/r_na", methods=["GET", "POST"])
def r_na():
    if request.method == "POST":

        if not request.form.get("ni") or not request.form.get("asset") or not request.form.get("wc"):
            x = 1
            return render_template("profitability_ratios.html", x=x)

        ni = float(request.form.get("ni"))
        asset = float(request.form.get("asset"))
        wc = float(request.form.get("wc"))

        ratio = ni / (asset + wc)

        return render_template("profitability_ratios.html", ratio=ratio)
    else:
        return render_template("profitability_ratios.html")

@app.route("/ra_r_c", methods=["GET", "POST"])
def ra_r_c():
    if request.method == "POST":

        if not request.form.get("ereturn") or not request.form.get("ec"):
            x = 1
            return render_template("profitability_ratios.html", x=x)

        ereturn = float(request.form.get("ereturn"))
        ec = float(request.form.get("ec"))

        ratio = ereturn / ec

        return render_template("profitability_ratios.html", ratio=ratio)
    else:
        return render_template("profitability_ratios.html")

@app.route("/amortisation", methods=["GET", "POST"])
def amortisation():
    if request.method == "POST":
        if not request.form.get("loan_amount") or not request.form.get("term") or not request.form.get("rate"):
            x = 1
            return render_template("amortisation.html", x=x)
        
        loan_amount = float(request.form.get("loan_amount"))
        term = int(request.form.get("term"))
        rate = float(request.form.get("rate"))
        period = str(request.form.get("period"))

        if period == "Monthly":
            monthly_rate = (rate * 0.01) / 12
            months = int(term * 12)

            monthly_payment = loan_amount * (monthly_rate * ((1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1))

            table = [{"period": 0, "payment": 0, "interest": 0, "principal": 0, "balance": loan_amount}]

            for i in range(1, months + 1):
                table.append(
                    {
                        "period": i,
                        "payment": monthly_payment,
                        "interest": table[i - 1]["balance"] * monthly_rate,
                        "principal": monthly_payment - (table[i - 1]["balance"] * monthly_rate),
                        "balance": abs(table[i - 1]["balance"] - (monthly_payment - (table[i - 1]["balance"] * monthly_rate)))
                    }
                )

            sum_interest = 0
            sum_principal = 0

            for i in range(len(table)):
                sum_interest += table[i]["interest"]
                sum_principal += table[i]["principal"]

            return render_template("amortisation.html", monthly_payment=monthly_payment, table=table, sum_interest=sum_interest, sum_principal=sum_principal, term=term, rate=rate, period=period)
        
        else:
            yearly_rate = rate * 0.01
            
            yearly_payment = loan_amount * (yearly_rate * ((1 + yearly_rate) ** term) / (((1 + yearly_rate) ** term) - 1))

            table = [{"period": 0, "payment": 0, "interest": 0, "principal": 0, "balance": loan_amount}]

            for i in range(1, term + 1):
                table.append(
                    {
                        "period": i,
                        "payment": yearly_payment,
                        "interest": table[i - 1]["balance"] * yearly_rate,
                        "principal": yearly_payment - (table[i - 1]["balance"] * yearly_rate),
                        "balance": abs(table[i - 1]["balance"] - (yearly_payment - (table[i - 1]["balance"] * yearly_rate)))
                    }
                )

            sum_interest = 0
            sum_principal = 0

            for i in range(len(table)):
                sum_interest += table[i]["interest"]
                sum_principal += table[i]["principal"]
            
            return render_template("amortisation.html", yearly_payment=yearly_payment, table=table, sum_interest=sum_interest, sum_principal=sum_principal, term=term, rate=rate, period=period)
    else:
        return render_template("amortisation.html")

@app.route("/npv", methods=["GET", "POST"])
def npv():
    if request.method == "POST":
        if not request.form.get("initial") or not request.form.get("rate") or not request.form.get("cf"):
            x = 1
            return render_template("npv.html", x=x)
    
        cfs = str(request.form.get("cf")).split(";")
        for cf in cfs:
            cf = cf.replace(".", "", 1)
            cf = cf.lstrip("-")
            if not cf.isdigit():
                y = 1
                return render_template("npv.html", y=y)

        cash_flows = []
        for cf in cfs:
            cash_flows.append(float(cf))

        initial = float(request.form.get("initial"))
        rate = float(request.form.get("rate"))
        period = len(cash_flows)

        table = [{"period": 0, "cash_flow": -initial, "present_value": -initial, "npv": -initial}]

        for i in range(len(cash_flows)):
            table.append(
                {
                    "period": i + 1,
                    "cash_flow": cash_flows[i],
                    "present_value": cash_flows[i] / ((1 + rate*0.01) ** (i + 1)),
                    "npv": table[i]["npv"] + (cash_flows[i] / ((1 + rate*0.01) ** (i + 1)))
                }
            )
        
        npv = 0
        for pv in table:
            npv += pv["present_value"]

        return render_template("npv.html", table=table, rate=rate, initial=initial, period=period, npv=npv)

    else:
        return render_template("npv.html")

@app.route("/dcf", methods=["GET", "POST"])
def dcf():
    if request.method == "POST":
        if not request.form.get("initial") or not request.form.get("rate") or not request.form.get("cf"):
            x = 1
            return render_template("dcf.html", x=x)        
        
        cfs = str(request.form.get("cf")).split(";")
        for cf in cfs:
            cf = cf.replace(".", "", 1)
            cf = cf.lstrip("-")
            if not cf.isdigit():
                y = 1
                return render_template("dcf.html", y=y)

        cash_flows = []
        for cf in cfs:
            cash_flows.append(float(cf))

        initial = float(request.form.get("initial"))
        rate = float(request.form.get("rate"))
        period = len(cash_flows)
        growth = float(request.form.get("growth"))

        if growth > rate:
            z = 1
            return render_template("dcf.html", z=z)

        table = [{"period": 0, "cash_flow": -initial, "present_value": -initial, "npv": -initial}]

        for i in range(len(cash_flows)):
            table.append(
                {
                    "period": i + 1,
                    "cash_flow": cash_flows[i],
                    "present_value": cash_flows[i] / ((1 + rate*0.01) ** (i + 1)),
                    "npv": table[i]["npv"] + (cash_flows[i] / ((1 + rate*0.01) ** (i + 1)))
                }
            )

        terminal = (cash_flows[period - 1] * (1 + growth * 0.01)) / (rate * 0.01 - growth * 0.01)
        terminal_pv = terminal / ((1 + rate * 0.01)**period)

        npv = terminal_pv 
        for pv in table:
            npv += pv["present_value"]

        table.append(
            {
                "period": "Terminal Value",
                "cash_flow": terminal,
                "present_value": terminal_pv,
                "npv": npv
            }
        )

        return render_template("dcf.html", table=table, rate=rate, initial=initial, period=period, npv=npv, terminal=terminal, growth=growth)

    else:
        return render_template("dcf.html")

if __name__ == "__main__":
    app.run(debug=True)