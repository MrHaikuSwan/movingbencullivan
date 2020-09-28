from lxml import html
import json

#open text document containing all saved Macro Review URLs
with open('macro_review_urls.txt', 'r') as f:
    macro_urls = f.readlines()
    macro_urls = [url.strip() for url in macro_urls]

#open text document containing all saved Micro Review URLs
with open('micro_review_urls.txt', 'r') as f:
    micro_urls = f.readlines()
    micro_urls = [url.strip() for url in micro_urls]

review_urls = macro_urls + micro_urls

# filepath to downloaded HTML: './TestBanks/{}l'.format('/'.join(url.split('/')[-3:]))
# filepath to JSON output: '.'.join(htmlpath.split('.')[:-1] + ['json'])

# starting with Micro Unit 1, AP Test Bank 1 for testing purposes
#url = "./TestBanks/APMicro/APU1/u1-1.html"

for url in review_urls:
    
    htmlpath = './ReviewBanks/{}l'.format('/'.join(url.split('/')[-2:]))
    jsonpath = '.'.join(htmlpath.split('.')[:-1] + ['json'])
    
    with open(htmlpath, 'r') as f:
        doc = html.fromstring(f.read())
    
    problems = doc.xpath('(//table)[1]/tbody/tr[@valign="baseline"]/td[@width="100%"]')
    questions = [problem.xpath('./div[1]')[0] for problem in problems]
    answer_choices = [problem.xpath('./div[2]/table/tbody/tr/td[2]//text()') for problem in problems]
    answers = [problem.xpath('./table/tbody/tr[1]/td[2]/div[1]/text()')[0] for problem in problems]
    
    urlbase = '/'.join(url.split('/')[:-1]) + '/'
    question_statements = [question.xpath('string(.)') for question in questions]
    images = [[urlbase + relurl for relurl in question.xpath('.//img/@src')] for question in questions]
    
    if len(set([len(question_statements), len(images), len(answer_choices), len(answers)])) > 1:
        raise Exception('Failed to properly parse HTML')
    else:
        nproblems = len(question_statements)
    
    output_JSON = []
    for qs, imgs, anschs, ans in zip(question_statements, images, answer_choices, answers):
        d = {}
        d['QuestionStatement'] = qs
        d['Images'] = imgs
        d['AnswerChoices'] = anschs
        d['Answer'] = ans
        output_JSON.append(d)
    
    with open(jsonpath, 'w') as f:    
        json.dump(output_JSON, f)