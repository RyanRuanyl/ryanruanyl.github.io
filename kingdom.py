import random

# 初始化国家状态
country_name = input("请输入您的国家名字：")+" 王国 "
population = 30
wealth = 100
happiness = 100
nobility_satisfaction = 0
international_reputation = 0
year = 1


# 定义小事件触发函数

def event_slaver():
    global population, wealth, happiness
    print("一位贵族请求将一些人变为奴隶，以提升国家财富。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        wealth += 15
        population -= 10
        happiness -= 10
        print("您同意了请求，财富增加了15，人口减少了10，但幸福度降低了10。")
    else:
        happiness += 5
        print("您拒绝了请求，国民感到安心，幸福度提高了5点。")


def event_migration():
    global population, wealth, happiness
    print("一艘满载移民的船抵达了您的港口，船上有许多人寻求庇护。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        population += 10
        wealth -= 15
        happiness -= 5
        print("您决定允许移民入境，国家人口增加了10，但财富减少了15，幸福度减少了5。")
    else:
        print("您拒绝了入境，但这没有影响。")


def event_disease():
    global population, wealth, happiness
    print("您的城市爆发了一场可怕的疫病，市民们急需医疗援助。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        happiness += 10
        wealth -= 15
        print("您决定建设医院救治感染者，幸福度增加了10，但财富减少了15。")
    else:
        population -= 15
        happiness -= 15
        print("您选择不隔离，这导致人口减少了15，同时幸福度降低了15。")


def event_orphan():
    global population, wealth, happiness
    print("一位大臣前来请求您资助当地的孤儿院，以帮助无家可归的孩子们。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        happiness += 5
        population += 10
        wealth -= 15
        print("您慷慨地决定资助孤儿院，国家的幸福度增加了5，人口增加了10，但财富减少了15。")
    else:
        happiness -= 10
        print("您拒绝了资助，这导致幸福度降低了10。")


def event_refugee():
    global population, wealth, happiness, international_reputation
    print("您的邻国陷入混乱，成千上万的难民涌入您的国家，寻求庇护。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        population += 10
        happiness -= 5
        wealth -= 10
        international_reputation += 10
        print("您决定接纳这些难民，您的国家人口增加了10，但幸福度减少了5，财富减少了10，国际声望增加10.")
    else:
        international_reputation -= 10
        print("您选择拒绝难民，国际声望减少10。")

def event_conscription():
    global wealth, population, happiness, international_reputation  # 添加 international_reputation
    print("您大臣建议征召国家的青年们入伍，以增强国家的军力。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        population -= 5
        wealth -= 10
        international_reputation += 10
        print("您决定实行强制征兵，国家劳动的人口减少了5，幸福度减少了10。你的武力威慑周边国家，国际声望增加10。")
    else:
        print("您拒绝了征兵，这没有影响。")

def event_loan():
    global wealth, international_reputation
    print("一位商人请求您的国家提供贷款以支持他参加国际的商业贸易。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        wealth += 20
        international_reputation += 20
        print("您同意提供贷款，国家的财富增加了20，国际声望增加了20。")
    else:
        print("您拒绝了贷款请求。")


def event_commander():
    global population, happiness
    print("您的军队领袖抓到了一些奴隶，询问是否将他们带回国家作为苦力。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        population += 15
        happiness -= 10
        print("您同意了这个提议，国家的人口增加了15，但幸福度减少了10。")
    else:
        happiness += 5
        print("您拒绝了这个提议，这导致幸福度增加了5。")


def event_tax_reform():
    global nobility_satisfaction, wealth, happiness
    print("贫富差距过大，国家的财政部门建议进行税收改革，以提高财富。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        wealth += 20
        happiness += 15
        nobility_satisfaction -= 20
        print("您决定进行税收改革，国家的财富增加了20，但幸福度增加了15，贵族利益冲突对你感到不满认可度减少20。")
    else:
        happiness -= 5
        print("您拒绝了税收改革，这导致幸福度减少了5。")


def event_scientist():
    global wealth, happiness, international_reputation
    print("一位科学家请求资金支持他的研究武器项目。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        wealth -= 20
        happiness -= 5
        international_reputation += 25
        print("您投资了科研，国家的幸福度增加了5，国际声望增加了25，但财富减少了20。")
    else:
        international_reputation -= 15
        print("您拒绝了资金支持，科技水平下降，国际声望减少15。")


def event_thieves():
    global wealth, happiness
    print("您国家的财政库遭到窃贼袭击，他们偷走了一大笔金钱。")
    choice = input("调查（A）或不予理会（B）？ ").lower()
    if choice == "a":
        if wealth >= 30:
            wealth -= 20
            happiness -= 5
            print("您调查了窃贼，成功找回了部分金钱，但财富减少了30，民众感到危机幸福度减少了5。")
        else:
            happiness -= 5
            print("您调查了窃贼，但没有找回金钱，幸福度减少了5。")
    else:
        wealth -= 30
        print("您选择不予理会，财富减少了30。")


def event_cultural_festival():
    global happiness, wealth, international_reputation  # 添加 international_reputation
    print("一位艺术家提出举办国家文化艺术节，以提高国民的幸福感。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        happiness += 10
        wealth -= 15
        international_reputation += 25
        print("您同意举办文化艺术节，国家的幸福度增加了10，国际声望增加了25，但财富减少了15。")
    else:
        happiness -= 10
        print("您拒绝了艺术节，幸福度减少了10。")


def event_nobles_privilege():
    global happiness, wealth, nobility_satisfaction, population  # 添加 population
    print("贵族们要求特权和特殊待遇。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        wealth += 50
        happiness -= 10
        print("您满足了贵族们的要求，国家的财富增加了50，但幸福度减少了10。")
    else:
        nobility_satisfaction -= 20
        happiness += 5
        print("您拒绝了贵族，贵族们对你认同感减少20，但幸福度略微增加了5。")


def event_poor_district():
    global wealth, happiness
    print("一位政府官员建议改善贫困地区的生活条件。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        happiness += 10
        wealth -= 15
        print("您决定改善贫困地区的生活条件，国家的幸福度增加了10，但财富减少了15。")
    else:
        happiness -= 5
        print("您拒绝了改善计划，民众幸福度减少5。")


def event_education_reform():
    global happiness, wealth, nobility_satisfaction
    print("您国家的教育系统需要改革，以提供更好的教育。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        happiness += 25
        wealth -= 15
        nobility_satisfaction -= 10
        print("您决定教育改革，国家的幸福度增加了25，但贵族阶级被冲击，贵族认同感减少了10，财富减少了15。")
    else:
        happiness -= 10
        print("您选择不改革，这导致幸福度降低了10。")


def event_free_market():
    global international_reputation, wealth, happiness, nobility_satisfaction
    print("一群商人请求您允许自由竞争的市场交易。")
    choice = input("同意（A）或拒绝（B）？ ").lower()
    if choice == "a":
        wealth += 20
        happiness += 10
        nobility_satisfaction -= 30
        print("您决定允许自由竞争，国家的财富增加了20，幸福度增加了10，但利益冲突，老牌贵族认同感减少了30。")
    else:
        wealth += 40
        happiness -= 5
        international_reputation -= 10
        print("您选择限制自由竞争，国际市场认为市场不自由，国际声望减少10，维护贵族利益，贵族给你分的利益，财富增加40，但阶级固化加剧，民众幸福度减少了5。")


# 新增国际声望、人口、幸福度和财富对游戏状态的影响
def update_game_state():
    global population, international_reputation, happiness, wealth

    # 处理国际声望
    if international_reputation < -50:
        print("国际声望过低，周边国家发动战争！")
        international_war()
    if international_reputation > 500:
        print("***世界中心，各国前来朝拜学习，当之无愧第一大国。***")
        population += 100
        wealth += 200
        happiness += 100
    if international_reputation > 300:
        print("***国家影响力巨大，各国前来学习。***")
        population += 50
        wealth += 50
        happiness += 30
    if international_reputation > 150:
        print("****世界贸易中心，人口增加30，财富增加50。****")
        population += 15
        wealth += 30

    # 处理人口
    if population > 600:
        happiness -= 300
    elif population > 500:
        happiness -= 150
    elif population > 400:
        happiness -= 80
    elif population > 300:
        happiness -= 50
    elif population > 150:
        happiness -= 20

    # 处理幸福度
    if happiness < -80:
        print("*****国家动荡，爆发起义！*****")
        uprising()

    if happiness < -50:
        print("****国家动荡，人民生活困难。*****")
        wealth -= 30

    if happiness < -30:
        print("****国民对您有些不满。****")

    if happiness > 300:
        print("*****幸福度正200时，国际天堂，人人向往，投资增多。******")
        population += 50
        wealth += 100

    if happiness > 150:
        print("*******幸福度正50时，国家幸福指数高，人口增加30，财富减少20。*******")
        population += 20
        wealth -= 10

    # 处理财富
    if wealth < -60:
        print("******国家破产，濒临王国危机，人口减少50。******")
        wealth -= 10
        population -= 20

    if wealth < -30:
        print("*****国家动荡，国际信用濒临破产，国民生活艰难，人口减少30。******")
        population -= 15

    if wealth < -15:
        print("******国民生活水平下降，对您有些不满。******")

    if wealth > 200:
        print("*******国际信用极高，贸易天堂，各国都来贸易。*****")
        population += 50
        wealth += 100

    if wealth > 150:
        print("***成为世界贸易中心，人口增加30，财富增加50。*****")
        population += 15
        wealth += 30


def international_war():
    global wealth, happiness, international_reputation

    # 计算战斗结果
    wealth_effect = 0 if wealth >= 0 else -1
    happiness_effect = 0 if happiness >= 0 else -1
    success_probability = 0.8 * (1 + wealth_effect) * (1 + happiness_effect)

    if random.random() < success_probability:
        print("您选择战斗，且幸运地赢得了战斗！")
        international_reputation += 20
    else:
        print("您选择战斗，但不幸输掉了战斗，国家支付大量赔款，民众生活困难！")
        wealth -= 30
        happiness -= 20


def uprising():
    global wealth, happiness, population

    # 计算起义结果
    wealth_effect = 0 if wealth >= 0 else -1
    happiness_effect = 0 if happiness >= 0 else -1
    success_probability = 0.3 * (1 + wealth_effect) * (1 + happiness_effect)

    if random.random() < success_probability:
        print("起义爆发，但您成功地平息了它！")
        happiness += 20
    else:
        print("起义爆发，您无法镇压，政权被推翻！")
        wealth = -100
        population = 0


# 游戏主循环
while True:
    print(f"\n----- 第 {year} 年 -----")
    print(f"国家：{country_name}")
    print(f"人口：{population}")
    print(f"财富：{wealth}")
    print(f"幸福度：{happiness}")
    print(f"国际声望：{international_reputation}")
    print(f"贵族认同感：{nobility_satisfaction}")

    # 更新游戏状态
    update_game_state()

    # 随机触发一个小事件
    random_event = random.choice([
        event_slaver, event_migration, event_disease, event_orphan,
        event_refugee, event_conscription, event_loan, event_commander,
        event_tax_reform, event_scientist, event_thieves, event_cultural_festival,
        event_nobles_privilege, event_poor_district, event_education_reform, event_free_market
    ])
    random_event()

    # 逐年推进游戏时间
    year += 1

    # 检查游戏结束条件
    if wealth >= 600:
        print("金币达到 600，国家富可敌国！")
        break
    elif wealth <= -100:
        print("金币陷入负债 100，国家破产！")
        break
    elif population <= 0:
        print("人口减少至 0，国家灭亡！")
        break
    elif happiness <= -80:
        print("幸福度降至负80，国家爆发起义！")
        break

print("游戏结束。")
