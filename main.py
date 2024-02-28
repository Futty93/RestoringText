import metaphone 
import sentenceFormat
import replace_word

if __name__ == '__main__':
    input_text = "Morning phone 1.3.3 Hold position. Traffic from final approach"
    formated_text = sentenceFormat.sentence_format(input_text)
    metaphone_key_array = metaphone.get_metaphone_key(formated_text)
    replaced_array = replace_word.replace_with_closest_words(metaphone_key_array)

    print(metaphone_key_array)
    print(replaced_array)