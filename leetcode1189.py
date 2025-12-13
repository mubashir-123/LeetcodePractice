text1 = "nlaebolko"
text2 = "loonbalxballpoon"
text3 = "balon"
target = 'ballon'
def maxNumberInstance(text: str,target: str) -> int:
    require_text = {}
    available_text = {}
    
    for c in target:
        require_text[c] = require_text.get(c,0) + 1
    
    for char in text:
        available_text[char] = available_text.get(char,0) + 1
    
    max_instance = float('inf')
    for item,required_num in require_text.items():
        available_num = available_text.get(item,0)
        possible_words = available_num // required_num
        max_instance = min(max_instance,possible_words)
    return max_instance

print(maxNumberInstance(text1,target))
print(maxNumberInstance(text2,target))
print(maxNumberInstance(text3,target))