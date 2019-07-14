######
# TREENODE CLASS
######
class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

    def traverse(self):
        story_node = self
        print(story_node.story_piece)
        while len(story_node.choices) > 0:
            user_choice = input("Enter 1 or 2 to continue to story: ")
            if user_choice in ['1', '2']:
                chosen_index = int(user_choice) - 1
                chosen_child = story_node.choices[chosen_index]
                print(chosen_child.story_piece)
                story_node = chosen_child


            else:
                "Invalid choice, enter 1 or 2: "


######
# VARIABLES FOR TREE
######

######
# TESTING AREA
######
# print("Once upon a time...")
story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")

# print(story_root.story_piece)
# user_choice = input("What is your name? ")
# print(user_choice)

choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

story_root.add_child(choice_a)
story_root.add_child(choice_b)
story_root.traverse()



