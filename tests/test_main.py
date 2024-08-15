from main import create_game
from unittest.mock import patch

def test_game_results():
    with patch('random.randrange', return_value=5):
        with patch('builtins.input', side_effect=['3', '4', '5']):
            result = create_game(1,10)
            assert result == 5
    
