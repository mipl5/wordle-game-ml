import requests

class CheckWord:
    url_string = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    reject = "No Definitions Found"
    
    def check_word(self, word: str) -> bool:
        check_string = f'{CheckWord.url_string}{word.lower()}'
        
        try:
            ans = requests.get(check_string, timeout=5)
            
            if ans.status_code == 200:
                data = ans.json()
                
                if isinstance(data, dict) and data.get('title') == self.reject:
                    return False
                
                return True
            
            elif ans.status_code == 404:
                return False
            
            else:
                return False
                
        except requests.exceptions.RequestException:
            return False