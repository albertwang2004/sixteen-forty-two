import random
import pygame

# Define the cards
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
suits = ['diamonds', 'hearts', 'spades', 'clubs'] # Cursed, but who cares

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("16.42")

def get_card_name(rank, suit):
    return rank + "_of_" + suit

# Load card images
card_images = {}
for rank in ranks:
    for suit in suits:
        card_name = get_card_name(rank, suit)
        card_images[card_name] = pygame.image.load(f"images/{card_name}.png")

while True:
    # Reset the timer
    time_offset = pygame.time.get_ticks() / 1000

    # Shuffle the deck
    deck = []
    for rank in ranks:
        for suit in suits:
            deck.append((rank, suit))
    random.shuffle(deck)

    assert len(deck) == 52, "Deck is not 52 cards, is " + str(len(deck)) + " cards instead."

    answer = get_card_name(*deck.pop())

    # Display each card image while erasing the last one, hitting enter to deal the next card
    card = deck.pop(0)
    done = False
    screen_pos = 0
    screen.fill((0, 0, 0))  # Clear the screen

    while not done:
        cards_left = len(deck)
        card_name = get_card_name(*card)
        card_image = card_images[card_name]

        # Scale down the card image
        scaled_card_image = pygame.transform.scale(card_image, (card_image.get_width() // 2, card_image.get_height() // 2))

        screen.blit(scaled_card_image, (50 - scaled_card_image.get_width() // 20 + screen_pos, 50 - scaled_card_image.get_height() // 20))

        # Display the number of cards left
        cards_left_text = pygame.font.SysFont("Courier New", 30).render(f"{cards_left} cards left", True, (255, 255, 255))
        # Wipe this area
        pygame.draw.rect(screen, (0, 0, 0), (screen_width - cards_left_text.get_width() - 100, screen_height - cards_left_text.get_height() - 100, cards_left_text.get_width() + 50, cards_left_text.get_height()))
        screen.blit(cards_left_text, (screen_width - cards_left_text.get_width() - 50, screen_height - cards_left_text.get_height() - 100))
        
        # Calculate the elapsed time
        elapsed_time = pygame.time.get_ticks() / 1000 - time_offset

        # Format the time as minutes and seconds
        time_text = pygame.font.SysFont("Courier New", 30).render(f"t = {elapsed_time:.3f}", True, (255, 255, 255))
        # Display the time in the bottom right corner
        pygame.draw.rect(screen, (0, 0, 0), (screen_width - cards_left_text.get_width() - 100, screen_height - time_text.get_height() - 50, cards_left_text.get_width() + 50, time_text.get_height()))
        screen.blit(time_text, (screen_width - time_text.get_width() - 50, screen_height - time_text.get_height() - 50))
        pygame.display.flip()  # Update the display

        # Detect pygame keyboard input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if len(deck) == 0:
                    done = True
                else:
                    card = deck.pop(0)
                    screen_pos += 4

            if event.type == pygame.QUIT:
                # Quit Pygame
                pygame.quit()
                exit()
        

    show_ans = False
    while done:
        # Display the answer
        screen.fill((0, 0, 0))  # Clear the screen

        if not show_ans:
            # Show a message in the center to think of the answer
            think_text = pygame.font.SysFont("Courier New", 30).render("Press space to reveal answer", True, (255, 255, 255))
            screen.blit(think_text, (screen_width // 2 - think_text.get_width() // 2, screen_height // 2 - think_text.get_height() // 2))

        else:
            answer_image = card_images[answer]
            # Scale it down
            scaled_answer_image = pygame.transform.scale(answer_image, (answer_image.get_width() // 3, answer_image.get_height() // 3))
            screen.blit(scaled_answer_image, (screen_width // 2 - scaled_answer_image.get_width() // 2, screen_height // 2 - scaled_answer_image.get_height() // 2))

            # Display a little text above to show that it's the answer
            answer_text = pygame.font.SysFont("Courier New", 30).render("Answer", True, (255, 255, 255))
            screen.blit(answer_text, (screen_width // 2 - answer_text.get_width() // 2, screen_height // 2 - scaled_answer_image.get_height() // 2 - answer_text.get_height() - 10))

            # Display elapsed time
            elapsed_time_text = pygame.font.SysFont("Courier New", 30).render(f"t = {elapsed_time:.3f}", True, (255, 255, 255))
            screen.blit(elapsed_time_text, (screen_width // 2 - elapsed_time_text.get_width() // 2, screen_height // 2 + scaled_answer_image.get_height() // 2 + 10))

            # Message beneath this saying space to restart
            if pygame.time.get_ticks() / 1000 - elapsed_time - time_offset > 1:
                restart_text = pygame.font.SysFont("Courier New", 30).render("Press space to restart", True, (255, 255, 255))
                screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2 + scaled_answer_image.get_height() // 2 + 10 + elapsed_time_text.get_height() + 10))

        pygame.display.flip()  # Update the display

        # Detect pygame keyboard input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if len(deck) == 0:
                    if show_ans and pygame.time.get_ticks() / 1000 - elapsed_time - time_offset > 1:
                        done = False
                    elif not show_ans:
                        show_ans = True
                        # Update elapsed time
                        elapsed_time = pygame.time.get_ticks() / 1000 - time_offset

            if event.type == pygame.QUIT:
                # Quit Pygame
                pygame.quit()
                exit()
