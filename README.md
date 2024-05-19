# Friend Trivia Game

This is a trivia game to play with friends.

## How to Play

To start, each player must include their name in the config.

When the program is run, a file will be generated for each player.
Each player should be provided their own file and should keep the contents
secret.

Players will take turns presenting a set of prompts (for example, 4 at a time). To 
present, a player will answer the prompt and pull up an image that represents the
answer that they chose. The player shows this image to the rest of the players and
has the rest of the players either provide a rating or answer the question. This
can be done on a countdown.

Once every player has answered the prompt, the player can reveal what the prompt
was. They will receive a point if the answer the player thought of matches the responses
to the prompt.

## Example

Assuming a game with 3 players and 1 prompt for each player:

Player 1 has the prompt: "A music artist / band that everybody would rate a 8-10"
Player 1 decides to answer with "All Time Low". They ask the rest of the players what they would rate the band.
Assuming every player rated the band with an 8/9/10, Player 1 will receive a point. Otherwise, they would continue to the 
next question.

The following is a sample of generated prompts:
```
A movie that nobody has seen
A song that everybody would rate a 4-6
An athletic activity that only Ross+Darian would rate a 0-3
A porn title that nobody would rate a 8-10
A TV show released in 2018 that everybody has seen
A movie released in 2023 that nobody has seen
An athletic activity that only Ross+David+Darian would rate a 8-10
A game that nobody would rate a 8-10
A music artist / band that Louie would say they like
A TV show released in 2017 that Darian has seen
```

The player would could come up with the following images and questions:
```
Les Miserables - "Have you seen this?"
Dance Dance - "What would you rate this?"
Pickleball - "What would you rate this?"
GRANDMA's FIRST TIME?!! - "What would you rate this?"
Cobra Kai - "Have you seen this?"
Open Heart - "Have you seen this?"
Running - "What would you rate this?"
Chivalry: Medieval Warfare - "What would you rate this?"
Hozier - "Do you like this?"
Young Sheldon - "Have you seen this?"
```

## Modifications

Within the config, there is room for modification to expand or simplify the game.

### Changing % Chances

|Config|Explanation|Default|
|---|---|---|
| ChanceFor_Everybody  | The % chance that the player component will be "everybody"  | 25% |
| ChanceFor_Nobody  | The % chance that the player component will be "nobody" | 25% |
|ChanceFor_ExtraPerson | The % chance that the player component can add an extra player. This will repeatedly add players until either the check fails, or there are no extra players | 33% |
|ChanceFor_OnlyPeople |The % chance that the player compoent will include "only" as a prefix, such as "only xyz players" | 33%|

### Topics

Topics can be added to the configuration to add more prompts. Topics consist of a few sections:

|Name|Description|Example|
|-|-|-|
|topic|The base prompt|A movie|
|modifiers|A list of modifications to append to the topic|released in 2018|
|modifier_chance|The % chance a modifier can be added to the topic|0.5|
|suffixes|The closing suffix of a prompt|that %1 %2 seen|


More topics can be freely added to the configuration JSON as well as modifiers, suffixes, and modifier % configuration.

#### Suffixes

For suffixes, %1 will be replaced with either
 - A player / group of players names
 - "nobody"
 - "everybody"

%2 will be replaced with either "have" or "has" depending on the number of players involved in %1 specified above.

Suffixes ending with "rate" will have a rating randomly chosen from the available pool in the configuration.
