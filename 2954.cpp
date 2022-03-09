#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

#define alphabet "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

using namespace std;

bool isLetter(const char l)
{
    for (char letter : alphabet)
    {
        if (letter == l)
            return true;
    }

    return false;
}

bool checkWord(const char letter, const char *word, int index)
{
    if (word[index] == letter)
    {
        return true;
    }
    return false;
}

bool resetScore(const char letter, const int letterIndex, bool &canBePerdi, bool &canBeJogo)
{

    if (canBePerdi)
    {
        canBePerdi = checkWord(letter, "perdi", letterIndex) or checkWord(letter, "PERDI", letterIndex);
    }

    if (canBeJogo)
    {
        canBeJogo = checkWord(letter, "jogo", letterIndex) or checkWord(letter, "JOGO", letterIndex);
    }

    if (letterIndex == 4 and canBePerdi)
    {
        return true;
    }
    if (letterIndex == 3 and canBeJogo)
    {
        return true;
    }

    return false;
}

int countScore(const char *sentence)
{
    int letterIndex{0}, sentenceIndex{0}, currentScore{0};
    vector<int> scores;
    bool resetScoreBool{false}, canBePerdi{true}, canBeJogo{true}, isLetterBool{true};
    char letter;

    while (sentence[sentenceIndex] != 0)
    {
        char letter = sentence[sentenceIndex];
        resetScoreBool = resetScore(letter, letterIndex, canBePerdi, canBeJogo);
        isLetterBool = isLetter(letter);

        if (isLetterBool)
        {
            currentScore++;
            letterIndex++;
        }
        else
        {
            letterIndex = 0;
            canBeJogo = true;
            canBePerdi = true;
        }

        if (resetScoreBool)
        {
            scores.push_back(currentScore);
            canBeJogo = true;
            canBePerdi = true;
            currentScore = 0;
        }

        sentenceIndex++;
    }

    scores.push_back(currentScore);
    int max = *max_element(scores.begin(), scores.end());
    return max;
}

int main()
{

    int N, score;
    string sentence;

    cin >> N;
    cin.ignore();

    for (int n = 0; n < N; n++)
    {
        getline(cin, sentence);
        score = countScore(sentence.c_str());
        cout << score << endl;
    }

    return 0;
}