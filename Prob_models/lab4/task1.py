from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re


class Bayesian_classifier:
    
    def __init__(self, sports_texts: list, politics_texts: list) -> None:
        self._sports_texts = sports_texts
        self._politics_texts = politics_texts

    # Preprocess the texts
    @staticmethod
    def clean_text(text: str):
        # Remove punctuation & convert to lowercase
        text = re.sub(r'[^\w\s]', '', text).lower()
        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        words = text.split()
        words = [word for word in words if word not in stop_words]
        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(word) for word in words]
        # Convert back to string
        text = ' '.join(words)
        return text

    # Preprocess the texts
    @staticmethod
    def preprocess_text(lst):
        cleaned_text_list = [Bayesian_classifier.clean_text(text) for text in lst]
        cleaned_text = ' '.join(cleaned_text_list)
        return cleaned_text

    def sports_dictionary(self, sports_counter: Counter) -> dict:
        words = Bayesian_classifier.preprocess_text(self._sports_texts).split()
        sports_counter.update(words)
        return dict(sports_counter)

    def politics_dictionary(self, politics_counter: Counter) -> dict:
        words = Bayesian_classifier.preprocess_text(self._politics_texts).split()
        politics_counter.update(words)
        return dict(politics_counter)

    def calculate_word_probability(word, category_dict, total_words):
        try:
            return (category_dict[word] + 1) / (total_words + len(category_dict))
        except KeyError:
            return 1 / (total_words + len(category_dict))

    # Classify the test texts
    def classify_text(self, test_text_arg) -> str:
        
        # Create the dictionaries
        sports_dict = Bayesian_classifier.sports_dictionary(self, Counter())
        politics_dict = Bayesian_classifier.politics_dictionary(self, Counter())

        # Calculate word probabilities
        sports_total_words = sum(sports_dict.values())
        politics_total_words = sum(politics_dict.values())
        words = Bayesian_classifier.clean_text(test_text_arg).split()

        # """bad example as this would introduce a bias towards a specific 
        # category before even considering the probabilities."""
        # sports_score = sports_total_words / (sports_total_words + politics_total_words)
        # politics_score = politics_total_words / (sports_total_words + politics_total_words)
        
        # for word in words:
            # sports_score *= Bayesian_classifier.calculate_word_probability(word, sports_dict, sports_total_words)
            # politics_score *= Bayesian_classifier.calculate_word_probability(word, politics_dict, politics_total_words)
        
        sports_score = 0
        politics_score = 0

        for word in words:
            sports_score += Bayesian_classifier.calculate_word_probability(word, sports_dict, sports_total_words)
            politics_score += Bayesian_classifier.calculate_word_probability(word, politics_dict, politics_total_words)

        if sports_score > 0 or politics_score > 0:
            if sports_score >= politics_score:
                return "Sports"
            else:
                return "Politics"
        else:
            return "Unclassified"
        
def main(correct_predictions: int):
    # Texts for creating the "Sports" dictionary
    sports_texts = [
        "Football is the most popular sport in the world.",
        "Tennis is an individual form of sport.",
        "The Champions League is one of the most prestigious football tournaments.",
        "Basketball is a team sport.",
        "Athletes spend a lot of time training."
    ]

    # Texts for creating the "Politics" dictionary
    politics_texts = [
        "Politics is the sphere of power and management of society.",
        "Elections are an important stage of the political process.",
        "Politicians make decisions that affect the lives of citizens.",
        "Parliament is a legislative body of power.",
        "Political parties represent different political views."
    ]

    # Texts for checking the work of the classifier
    test_texts = [
        "A football player won a gold medal at the Olympic Games.",
        "The political party announced its program.",
        "The tennis player received an award for winning the tournament.",
        "Parliament passed a new law.",
        "The athlete became a record holder in high jump.",
        "The politician made a public speech.",
        "The football match ended in a draw.",
        "The political leader expressed his position on the event.",
        "Basketball players won the championship.",
        "The legislative committee is considering amendments to the law.",
    ]
    
    # Expected texts for checking accuracy of the classifier
    test_texts_expected = [
        ("A football player won a gold medal at the Olympic Games.", "Sports"),
        ("The political party announced its program.", "Politics"),
        ("The tennis player received an award for winning the tournament.", "Sports"),
        ("Parliament passed a new law.", "Politics"),
        ("The athlete became a record holder in high jump.", "Sports"),
        ("The politician made a public speech.", "Politics"),
        ("The football match ended in a draw.", "Sports"),
        ("The political leader expressed his position on the event.", "Politics"),
        ("Basketball players won the championship.", "Sports"),
        ("The legislative committee is considering amendments to the law.", "Politics")
    ]

    b: Bayesian_classifier = Bayesian_classifier(sports_texts, politics_texts)
    
    # Test the classifier
    for text, expected_category in test_texts_expected:
        classification = b.classify_text(text)
        if classification == expected_category:
            correct_predictions += 1
        print(f"Text: {text}\nExpected Category: {expected_category}\nPredicted Category: {classification}\n")

    accuracy = correct_predictions / len(test_texts) * 100
    print("Accuracy: {:.1f}%".format(accuracy))
    
if __name__ == "__main__":
    main(0)