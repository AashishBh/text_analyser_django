from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("hello <h1>World </h1>")


def about(request):
    return HttpResponse("about page")


def removeLine(userInput):
    refined_text = ""
    for char in userInput:
        if char!= '\n' and char!='\r':
            refined_text += char
    return refined_text

def removePunc(userInput):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    refined_text = str()
    for ele in userInput:
        if ele not in punc:
            refined_text = refined_text + ele
    return refined_text

def removeExtraSpace(userInput):
    tempText = str()
    for x in range(len(userInput)):
        if not (userInput[x] == ' ' and userInput[x+1] == ' '):
            tempText += userInput[x]
    return tempText

def analyser(request):
    # boxtext = request.GET.get('box','default')
    # check_box = request.GET.get('check','off')
    # capitalise = request.GET.get('capitalise','off')
    # charcounter = request.GET.get('charcounter','off')
    # count = 0
    # if check_box == 'on' and capitalise == 'on':
    #     refined_text = str()
    #     # punctuation remover
    #     punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #     for ele in boxtext:
    #         if ele not in punc:
    #             refined_text = refined_text + ele
    #     params = {'boxtext':boxtext, 'refined_text':refined_text, 'capitalised_text': boxtext.upper()}
    #     return render(request,'analyser.html',params)
    # if charcounter == 'on':
    #     for x in boxtext:
    #         count+=1
    #     params = {'boxtext':boxtext,'count':count}
    #     return render(request,'analyser.html',params)
    # else:
    #     return HttpResponse("Checkbox not selected")
    textareaText = request.POST.get('box', 'default')
    # print(textareaTextList)
    # textareaText = str()
    # print(textareaText)
    # for x in textareaTextList:
    #     textareaText = textareaText + "\n" + x
    # print(textareaText)
    # print(len(textareaText))
    removePunctuation = request.POST.get('removePunc','off')
    capitalise = request.POST.get('capitalise', 'off')
    lineRemover = request.POST.get('lineRemover', 'off')
    extraSpaceRemover = request.POST.get('extraSpaceRemover', 'off')
    print(lineRemover)
    refinedText = str()
    if removePunctuation == 'on':
        refinedText = removePunc(textareaText)
        if capitalise == 'on':
            refinedText = refinedText.upper()
        if lineRemover == 'on':
            refinedText = removeLine(refinedText)
        if extraSpaceRemover == 'on':
            refinedText = removeExtraSpace(refinedText)
    elif capitalise == 'on':
        refinedText = textareaText.upper()
        if lineRemover == 'on':
            refinedText = removeLine(refinedText)
        if extraSpaceRemover == 'on':
            refinedText = removeExtraSpace(refinedText)
    elif lineRemover == 'on':
        refinedText = removeLine(textareaText)
        print(textareaText.index('\n'))
        if extraSpaceRemover == 'on':
            refinedText = removeExtraSpace(refinedText)
    elif extraSpaceRemover == 'on':
        refinedText = removeExtraSpace(textareaText)
    else:
        refinedText = textareaText

    params = {'''userInput''': textareaText , 'refinedText':refinedText}
    return render(request, 'analyser.html', params)

def file(request):
    f = open("textutils/one.txt", "r")
    return HttpResponse(f.read())

def charCounter(request):
    return render(request, 'charcounter.html')


def navigator(request):
    return HttpResponse('''
    <h1>My Personal Navigator </h1>
    <p> <a href = "https://www.facebook.com">Facebook </a></p>
    <p> <a href = "https://www.instagram.com">Instagram </p>
    <p> <a href = "https://www.twitter.com">Twitter </p>
    <p> <a href = "https://www.reddit.com">Reddit </p>
    <p> <a href = "https://www.telegram.org">Telegram </p>
    ''')