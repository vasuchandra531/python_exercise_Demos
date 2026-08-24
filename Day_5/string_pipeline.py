#Case Conversions & Text Normalization
model_output="ai is the Future of everything"
print(model_output.upper())
print(model_output.lower())
print(model_output.capitalize())
print(model_output.title())

# Whitespace & Character Stripping
response="   ???Hello Human???   "
print(response.strip())
print(response.strip(" ?"))


#Substring Replacement & Case-Insensitive Counting
text = "ML is a critical component of the modern AI. ML techniques are advancing rapidly."
print(text.replace("ML","Machine Learning"))

#Count of string
count_text = "AI is the Future. Embrace the future of AI."
print(count_text.count("future"))
print(count_text.lower().count("future"))

#String Splitting, Joining, Prefix/Suffix Removal, & Immutability
text="a breakthrough at every step"
print(text.split()) # splitting
text1=['AI', 'ML', 'genai', 'LLM', 'NLP']
ml_terms=",".join(text1) #join
print(ml_terms)

#Prefix
url="https://example.com"
domain_url=url.removeprefix("https://")
print(domain_url)

#Suffix
filename="state_of_AI_2025.pdf"
file_name=filename.removesuffix(".pdf")
print(file_name)

#prove Immutability of the string
filename="state_of_AI_2025.pdf"
filename.removesuffix(".pdf")
print(filename)

#Indexing, Concatenation, Repetition, & Slicing
#in index form is start form 0 to n
message = "GenAI is amazing"
print(message[0])
print(message[5])
print(message[4])
print(message[1])
print(message[15])
#But in the reverse index it start from -1
print(message[-1])
print(message[-15])
print(message[-16])

#Concatenation
greeting ="Hello,"
role="GenAI is amazing"
full_greeting=greeting+role+'!'
print(full_greeting)

#Repetition
separator="??"
print(separator *30)

#Multi-Parameter Slicing
sub="Machine Learning"
print(sub[0:7])
print(sub[7:])
print(sub[:7])
print(sub[13:])
print(sub[::2])
print(sub[::-1])


