import pyautogui
import pygetwindow as gw
import time

def open_spotify_via_start_menu():
    print("Opening Start Menu...")
    pyautogui.hotkey('win')
    time.sleep(1)
    
    print("Typing 'Spotify' in the Start Menu...")
    pyautogui.write('Spotify')
    time.sleep(1)
    
    print("Opening Spotify application...")
    pyautogui.press('enter')
    time.sleep(6)  

def focus_spotify_window():
    print("Searching for Spotify window...")
    spotify_windows = [window for window in gw.getAllTitles() if 'Spotify' in window]
    
    if spotify_windows:
        try:
            spotify_window = gw.getWindowsWithTitle(spotify_windows[0])[0]
            spotify_window.restore()  
            spotify_window.activate()  
            time.sleep(2)  
            print(f"Spotify window focused: {spotify_windows[0]}")
        except Exception as e:
            print(f"Error focusing Spotify window: {e}")
            return False
    else:
        print("Spotify window not found.")
        return False
    return True

def play_song_in_spotify(song_name):
    open_spotify_via_start_menu()
    
    if focus_spotify_window():
        print("Focusing search bar...")
        pyautogui.hotkey('ctrl', 'l')  
        time.sleep(3) 
        
        print(f"Typing the song name: {song_name}")
        pyautogui.write(song_name)
        time.sleep(3)
        
        pyautogui.press('enter') 
        print("Searching for the song...")
        time.sleep(5)  
        
        play_button_x, play_button_y = 1272, 677  # coordinates for the green Play button
        print(f"Clicking the Play button at ({play_button_x}, {play_button_y})")
        
        pyautogui.moveTo(play_button_x, play_button_y)
        pyautogui.doubleClick()()  # click the first song 
        
        print(f"Playing: {song_name}")
    else:
        print("Failed to focus on the Spotify window.")

# def pause_spotify():
#     if focus_spotify_window():
#         print("Pausing Spotify...")
#         pyautogui.press('space')  

# if __name__ == "__main__":
#     song = "Believer"
#     play_song_in_spotify(song)
#     time.sleep(5)  # Let the song play for a few seconds
#     pause_spotify()  # Pause the song after 5 seconds

    # X=1272, Y=677
