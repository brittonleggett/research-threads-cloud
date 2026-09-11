# -*- coding: utf-8 -*-
"""Generates a Qualtrics Advanced-Format .txt import file from
Study2_Qualtrics_Instrument_READY_2026-09-09.md + notes/2026-08-04-vignette-drafts-v1.md.

Import path in Qualtrics: Create new project -> Survey -> "Import a survey file" -> select the .txt.
Advanced Format carries blocks, questions, choices and export tags. It does NOT carry Survey Flow
(randomizer, branch logic, embedded data) -- those are in the companion post-import checklist.
"""
import io

L7_SD_SA = ['1 - Strongly disagree', '2', '3', '4', '5', '6', '7 - Strongly agree']
L7_SA_SD = ['1 - Strongly agree', '2', '3', '4', '5', '6', '7 - Strongly disagree']
L7_VHI_VLO = ['1 - Very high', '2', '3', '4', '5', '6', '7 - Very low']

o = io.StringIO()
w = o.write

w('[[AdvancedFormat]]\n\n')
w('[[ED:AttributionFrame]]\n[[ED:CostResponse]]\n[[ED:AttentionCheckPass]]\n[[ED:ManipCheck1Correct]]\n\n')

# ---------------- Block 1: Consent ----------------
w('[[Block:Consent]]\n\n')
w('[[Question:DB]]\n[[ID:consent_text]]\n')
w('&lt;PASTE THE FULL TEXT OF Informed_Consent_Tariffs.docx HERE.&gt;<br><br>'
  'This survey takes approximately 12 minutes.\n\n')
w('[[Question:MC:SingleAnswer:Vertical]]\n[[ID:consent]]\n')
w('Do you agree to participate in this study?\n')
w('[[Choices]]\nI agree to participate\nI do not agree to participate\n\n')
w('[[PageBreak]]\n\n')

# ---------------- Block 2: Screener ----------------
w('[[Block:Screener]]\n\n')
w('[[Question:TE:SingleLine]]\n[[ID:age_screen]]\nWhat is your age in years?\n\n')
w('[[Question:MC:SingleAnswer:Vertical]]\n[[ID:us_resident]]\n')
w('Do you currently reside in the United States?\n[[Choices]]\nYes\nNo\n\n')
w('[[Question:Matrix:SingleAnswer]]\n[[ID:attn_check]]\n')
w('Please indicate how much you agree with each of the following statements.\n')
w('[[Choices]]\n')
w('I pay attention to details when reading online.\n')
w('To show you are reading carefully, please select "Somewhat agree" for this item.\n')
w('I often shop at national retail chains.\n')
w('[[Answers]]\n')
for a in ['Strongly disagree', 'Disagree', 'Somewhat disagree', 'Neither agree nor disagree',
          'Somewhat agree', 'Agree', 'Strongly agree']:
    w(a + '\n')
w('\n[[PageBreak]]\n\n')

# ---------------- Block 3: Vignettes (6 blocks) ----------------
SHARED = ('Imagine you are a regular customer of Meridian Home, a national retailer where you often '
          'shop. You receive the following email from the company:<br><br><b>Subject: An Update on '
          'Pricing at Meridian Home</b><br><br>')

CELLS = [
 (1, 'TariffExplicit_FullPassThrough', 'explicit', 'pass-through',
  'As you may have seen in the news, new tariffs on imported goods have significantly increased the '
  'cost of many of the products we sell. Because of these tariff-related costs, we are raising prices '
  'on select items starting next month. These increases reflect the full amount of the added tariff '
  'costs we are now paying to bring these products to you.'),
 (2, 'TariffExplicit_SharedBurden', 'explicit', 'absorption',
  'As you may have seen in the news, new tariffs on imported goods have significantly increased the '
  'cost of many of the products we sell. Because of these tariff-related costs, we are raising prices '
  'on select items starting next month. We are absorbing a significant portion of these added tariff '
  'costs ourselves, and only passing along part of the increase to our customers.'),
 (3, 'GeneralCost_FullPassThrough', 'vague', 'pass-through',
  'Due to rising costs across our supply chain, the cost of many of the products we sell has '
  'significantly increased. Because of these higher costs, we are raising prices on select items '
  'starting next month. These increases reflect the full amount of the added costs we are now paying '
  'to bring these products to you.'),
 (4, 'GeneralCost_SharedBurden', 'vague', 'absorption',
  'Due to rising costs across our supply chain, the cost of many of the products we sell has '
  'significantly increased. Because of these higher costs, we are raising prices on select items '
  'starting next month. We are absorbing a significant portion of these added costs ourselves, and '
  'only passing along part of the increase to our customers.'),
 (5, 'Silent_FullPassThrough', 'silent', 'pass-through',
  'We value you as a customer and want to keep you informed about changes at Meridian Home. Prices on '
  'select items will be increasing starting next month. This adjustment reflects the full increase in '
  'what it now costs us to bring these products to you. We appreciate your continued business and look '
  'forward to serving you.'),
 (6, 'Silent_SharedBurden', 'silent', 'absorption',
  'We value you as a customer and want to keep you informed about changes at Meridian Home. Prices on '
  'select items will be increasing starting next month. We are absorbing a significant portion of the '
  'increase in what it now costs us to bring these products to you, and only passing along part of it. '
  'We appreciate your continued business and look forward to serving you.'),
]

for n, name, frame, resp, body in CELLS:
    w('[[Block:Vignette %d - %s]]\n\n' % (n, name))
    w('[[Question:DB]]\n[[ID:vig%d]]\n' % n)
    w(SHARED + body + '\n\n')
    w('[[PageBreak]]\n\n')

# ---------------- Block 4: Manipulation checks ----------------
w('[[Block:Manipulation Checks]]\n\n')
w('[[Question:MC:SingleAnswer:Vertical]]\n[[ID:mc_reason]]\n')
w('According to the message, what did the company say was the reason for the price increase?\n')
w('[[Choices]]\nTariffs\nGeneral rising costs\nNo reason given\nDon\'t recall\n\n')
w('[[Question:MC:SingleAnswer:Horizontal]]\n[[ID:mc_clarity]]\n')
w('How clearly did the message explain the reason for the price increase?\n[[Choices]]\n')
for a in ['1 - Not at all clearly', '2', '3', '4', '5', '6', '7 - Very clearly']:
    w(a + '\n')
w('\n[[Question:MC:SingleAnswer:Vertical]]\n[[ID:mc_costresp]]\n')
w('According to the message, is the company passing along the full cost increase, or absorbing part of it?\n')
w('[[Choices]]\nFull amount\nPartial, company absorbing some\nUnclear\n\n')
w('[[PageBreak]]\n\n')

# ---------------- Block 5: Fairness ----------------
w('[[Block:Perceived Price Fairness]]\n\n')
w('[[Question:MC:SingleAnswer:Horizontal]]\n[[ID:fair_1]]\n')
w('How would you rate the price increase described in the message?\n[[Choices]]\n')
for a in ['1 - Very fair', '2', '3', '4', '5', '6', '7 - Very unfair']:
    w(a + '\n')
w('\n[[Question:MC:SingleAnswer:Horizontal]]\n[[ID:fair_2_R]]\n')
w('"This price is not fair."<br><i>(Reverse-scored before averaging with the item above.)</i>\n[[Choices]]\n')
for a in L7_SA_SD:
    w(a + '\n')
w('\n[[PageBreak]]\n\n')

# ---------------- Block 6: Opportunism ----------------
w('[[Block:Perceived Opportunism]]\n\n')
w('[[Question:MC:SingleAnswer:Horizontal]]\n[[ID:opp_1]]\n')
w('How would you rate the company\'s motive in this situation?\n[[Choices]]\n')
for a in ['1 - Bad', '2', '3', '4', '5', '6', '7 - Good']:
    w(a + '\n')
w('\n[[Question:MC:SingleAnswer:Horizontal]]\n[[ID:opp_2]]\n')
w('"The intent in this situation was to take advantage of you (the customer)."\n[[Choices]]\n')
for a in L7_SA_SD:   # AS SPECIFIED, unflipped -- see OPEN DECISION 1 in the checklist
    w(a + '\n')
w('\n[[PageBreak]]\n\n')

# ---------------- Block 7: Trust ----------------
w('[[Block:Trust in the Company]]\n\n')
w('[[Question:Matrix:SingleAnswer]]\n[[ID:trust]]\n')
w('Please indicate how much you agree with each statement about Meridian Home.\n[[Choices]]\n')
for s in ['I trust this company.', 'I rely on this company.', 'This is an honest company.',
          'This company is safe.']:
    w(s + '\n')
w('[[Answers]]\n')
for a in L7_SD_SA:
    w(a + '\n')
w('\n[[PageBreak]]\n\n')

# ---------------- Block 8: Purchase Intention ----------------
w('[[Block:Purchase Intention]]\n\n')
w('[[Question:MC:SingleAnswer:Horizontal]]\n[[ID:pi_1]]\n')
w('The likelihood of purchasing this product is:\n[[Choices]]\n')
for a in L7_VHI_VLO:
    w(a + '\n')
w('\n[[Question:Matrix:SingleAnswer]]\n[[ID:pi_23]]\n')
w('Please indicate how much you agree with each statement.\n[[Choices]]\n')
w('If I were going to buy this product, I would consider buying this product at the price shown.\n')
w('At the price shown, I would consider buying the product.\n')
w('[[Answers]]\n')
for a in L7_SD_SA:
    w(a + '\n')
w('\n[[Question:MC:SingleAnswer:Horizontal]]\n[[ID:pi_4]]\n')
w('The probability that I would consider buying the product is:\n[[Choices]]\n')
for a in L7_VHI_VLO:
    w(a + '\n')
w('\n[[Question:MC:SingleAnswer:Horizontal]]\n[[ID:pi_5]]\n')
w('My willingness to buy the product is:\n[[Choices]]\n')
for a in L7_VHI_VLO:
    w(a + '\n')
w('\n[[PageBreak]]\n\n')

# ---------------- Block 9: WOM ----------------
w('[[Block:Word-of-Mouth Intention]]\n\n')
w('[[Question:MC:SingleAnswer:Horizontal]]\n[[ID:wom_1]]\n')
w('How likely are you to spread positive word-of-mouth about Meridian Home?\n[[Choices]]\n')
for a in ['1 - Very unlikely', '2', '3', '4', '5', '6', '7 - Very likely']:
    w(a + '\n')
w('\n[[Question:Matrix:SingleAnswer]]\n[[ID:wom_23]]\n')
w('Please indicate how much you agree with each statement.\n[[Choices]]\n')
w('I would recommend Meridian Home\'s products to my friends.\n')
w('If my friends were looking for a product like this, I would tell them to try Meridian Home.\n')
w('[[Answers]]\n')
for a in L7_SD_SA:
    w(a + '\n')
w('\n[[PageBreak]]\n\n')

# ---------------- Block 10: Demographics ----------------
w('[[Block:Demographics]]\n\n')
w('[[Question:TE:SingleLine]]\n[[ID:age]]\nWhat is your age in years?\n\n')
w('[[Question:MC:SingleAnswer:Vertical]]\n[[ID:gender]]\nWhat is your gender?\n[[Choices]]\n')
for c in ['Male', 'Female', 'Non-binary', 'Prefer to self-describe', 'Prefer not to say']:
    w(c + '\n')
w('\n[[Question:MC:SingleAnswer:Vertical]]\n[[ID:income]]\nWhat is your annual household income?\n[[Choices]]\n')
for c in ['Less than $25,000', '$25,000 - $49,999', '$50,000 - $74,999', '$75,000 - $99,999',
          '$100,000 - $149,999', '$150,000 or more', 'Prefer not to say']:
    w(c + '\n')
w('\n[[Question:MC:SingleAnswer:Vertical]]\n[[ID:education]]\n')
w('What is the highest level of education you have completed?\n[[Choices]]\n')
for c in ['Less than high school', 'High school diploma or GED', 'Some college, no degree',
          "Associate's degree", "Bachelor's degree", 'Graduate or professional degree']:
    w(c + '\n')
w('\n[[Question:MC:SingleAnswer:Vertical]]\n[[ID:shop_freq]]\n')
w('How often do you shop at retailers like the one described in this study?\n[[Choices]]\n')
for c in ['Never', 'Rarely (a few times a year)', 'Occasionally (monthly)',
          'Regularly (a few times a month)', 'Frequently (weekly or more)']:
    w(c + '\n')
w('\n[[Question:MC:SingleAnswer:Horizontal]]\n[[ID:ideology]]\n')
w('In general, how would you describe your political views?\n[[Choices]]\n')
for a in ['1 - Very liberal', '2', '3', '4 - Moderate', '5', '6', '7 - Very conservative']:
    w(a + '\n')
w('\n[[PageBreak]]\n\n')

# ---------------- Block 11: Debriefing ----------------
w('[[Block:Debriefing]]\n\n')
w('[[Question:DB]]\n[[ID:debrief]]\n')
w('&lt;PASTE THE FULL TEXT OF notes/2026-08-04-debriefing-statement.md HERE.&gt;<br><br>'
  'Please note: "Meridian Home" is a fictional company created for this study, and the email you '
  'read was written by the researchers. It does not describe any real company or any real pricing '
  'decision.\n\n')

out = r'C:/Users/britt/Desktop/Claude Global/TARIFF_PAPER/Study2_Qualtrics_IMPORT_2026-09-11.txt'
open(out, 'w', encoding='utf-8').write(o.getvalue())

txt = o.getvalue()
print('written:', out)
print('bytes:', len(txt))
print('blocks:', txt.count('[[Block:'))
print('questions:', txt.count('[[Question:'))
print('export tags:', txt.count('[[ID:'))
