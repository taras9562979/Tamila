text = '   try   my ---   '
print(f'text -> {text} {len(text)}')
print(f'text.strip() -> {text.strip()} {len(text.strip())}')
print(f'text.strip() -> {text.strip(" -")} {len(text.strip(" -"))}')

text_2 = 'The global chatbot market size is forecasted to grow from US$2.6B in 2019 to US$9.4B by 2024, at a CAGR of 29.7%'
print(f'text_2 -> {text_2} \n{len(text_2)}')
print(f'text_2.split(" ") -> {text_2.split(" ")}')