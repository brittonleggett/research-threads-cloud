# -*- coding: utf-8 -*-
"""Builds an OPTIONAL v2 Qualtrics import from the locked 2026-09-11 import file.
Does NOT touch the original. Two changes, both Britton's pending calls (notes 2026-11-12, 2026-11-17):
 (a) insert Block 4b (locus / controllability / blame) after Manipulation Checks;
 (b) flip Opportunism item 2 anchors to Disagree->Agree (1->7), so the instrument has no backward scale.
 NOTE (b): after flipping, opp_2 is scored directly (higher = more opportunism); the Opportunism motive item opp_1
 (Bad=1..Good=7) is then the reverse-keyed one in analysis. Check scoring before fielding.
Block 4b wording is the author's own draft, NOT a validated scale; label it so in methods."""
import sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8').read()
b4b = ('[[Block:Attribution of Responsibility (draft)]]\n\n'
 '[[Question:MC:SingleAnswer:Horizontal]]\n[[ID:attr_external]]\n'
 'How much was the price increase due to factors outside the company\'s control?\n[[Choices]]\n'
 '1 - Not at all\n2\n3\n4\n5\n6\n7 - Completely\n\n'
 '[[Question:MC:SingleAnswer:Horizontal]]\n[[ID:attr_avoidable]]\n'
 'How much could the company have avoided this price increase?\n[[Choices]]\n'
 '1 - Not at all\n2\n3\n4\n5\n6\n7 - Completely\n\n'
 '[[Question:Matrix:SingleAnswer]]\n[[ID:attr_resp]]\n'
 'How responsible is each of the following for the price increase?\n[[Choices]]\n'
 'The company\nThe government\nOther factors\n[[Answers]]\n'
 '1 - Not at all\n2\n3\n4\n5\n6\n7 - Completely\n\n'
 '[[PageBreak]]\n\n')
m = '[[Block:Perceived Price Fairness]]'
assert t.count(m) == 1
t = t.replace(m, b4b + m)
old = ('"The intent in this situation was to take advantage of you (the customer)."\n[[Choices]]\n'
       '1 - Strongly agree\n2\n3\n4\n5\n6\n7 - Strongly disagree\n')
new = old.replace('1 - Strongly agree', '1 - Strongly disagree').replace('7 - Strongly disagree', '7 - Strongly agree')
assert t.count(old) == 1, 'opp_2 anchors not found as expected'
t = t.replace(old, new)
open(dst, 'w', encoding='utf-8').write(t)
print('blocks', t.count('[[Block:'), 'questions', t.count('[[Question:'))
