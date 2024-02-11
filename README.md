# Bedrock-testing
## Listing models:
```bash
aws bedrock list-foundation-models  --profile <AWS PROFILE> |jq -r '.modelSummaries | .[].modelId'
```
# Testing AWS Bedrock service
## Basic test
Testing basic functionality of AWS Bedrock in Bash
Using [basic-test.sh](basic-test.sh): `bash basic-test.sh <AWS Profile> <Prompt>`.
### Bash basic tests
```bash
% bash basic-test.sh botdev "tell me a story"
{
    "contentType": "application/json"
}
{
  "generations": [
    {
      "finish_reason": "COMPLETE",
      "id": "04ef60f8-6cb6-4951-a23a-f54d51bbc764",
      "text": " Once upon a time, in a faraway kingdom, there lived a brave and fearless princess named Aurora. \n\n Aurora was an extraordinary girl, born under the night sky, under the lucky star, the Dandelion. From birth, she was imbued with extraordinary powers that set her apart from others. The powers of love, they said.\n\n \nAs she grew older, Aurora became aware of her unique abilities. She could sense the love in the air, feel it surrounding her, and see it glowing in the hearts of those around her. It was a special kind of magic that she could not explain, but it was her most cherished gift.\n\n \nOne day, as she was walking through the castle, she met a handsome prince, who was as kind and gentle as the moonlight. His name was Prince Philip, and they fell in love at first sight. The love that they felt was so strong, so pure, so true, that it was like nothing either of them had ever experienced before.\n\n \nAs their love grew stronger, they decided to get married and start a new life together. But as fate would have it, the evil Queen Maleficent, who had a grudge against the princess for unknown reasons, was not pleased by the arrival of the new love in the kingdom. She did what she could to keep the princess away from Prince Philip, using her dark magic to create obstacles and challenges for the young couple.\n\n \nDespite all the obstacles, Aurora and Philip remained determined to be together. They fought against the dark forces that threatened their love, and in the end, they emerged victorious. Their love triumphed over evil, and they lived happily ever after, united by their bond and the power of their love.\n\n \nAnd so, Aurora became the queen of hearts, not just by birthright, but by her own actions and the love she shared with her people, a true symbol of hope and love, a legend to be passed on for generations to come. \n\nThe end. "
    }
  ],
  "id": "b6ffce90-4792-4078-9532-5c932fe7fd51",
  "prompt": "tell me a story"
}
```
### Python basic test
Testing basic functionality of AWS Bedrock in Python
Using [basic-test.py](basic-test.py): `python3 basic-test.py <AWS Profile> <Prompt>`.

```bash
% python3 basic-test.py botdev "tell me a story" 
{
    "generations": [
        {
            "finish_reason": "COMPLETE",
            "id": "2280bf4d-6b86-4038-b41e-bf7a1f08ab9e",
            "text": " Once upon a time, in a faraway land, there lived a young boy named Timmy. Timmy was an adventurous soul, filled with curiosity and a love for exploring the world around him.  \n  \nOne sunny day, as Timmy was playing in his backyard, he noticed a small, old door hidden in the dense bushes. Intrigued by its mysterious appearance, he cautiously opened it, and to his surprise, he found himself in a magical forest! The trees were taller and more colorful than he had ever seen, and the animals seemed to be from a different world, their fur and feathers vibrant and shiny.\n\n  \nAs Timmy made his way through the forest, he met all sorts of characters: a wise old owl who lived in a treehouse and provided him with clues to navigate through the forest, a group of friendly fairies who lived in a hidden clearing and showed him where to find the rare and magical fruits, and a wise old tortoise who shared insightful tales of past heroes and their journeys.\n\n \nAs Timmy continued on his journey, he discovered that the forest was full of challenges and obstacles, but he never gave up. With his courage and determination, he overcame every obstacle and emerged victorious. Finally, at the end of the forest, he found a magical portal that led him back to his own world, where he was greeted with a hero's welcome by his family and friends.\n\n \nTimmy learned that the true power of adventure is not about the destination, but about the journey itself. He gained valuable lessons in courage, perseverance, and friendship, and he knew that he would always cherish the memories of his magical journey through the mysterious forest."
        }
    ],
    "id": "e3a8f205-31ab-48e1-918c-342d0a2dbaab",
    "prompt": "tell me a story"
}
```
## Cloudwatch query test

Testing Cloudwatch query generation using AWS Bedrock in Python
Using [cloudwatch-titan-test.py](cloudwatch-titan-test.py): `python3 cloudwatch-titan-test.py <AWS Profile> <Request>`.

To get the model to accurately create a Cloudwatch query, an [instructions file](cloudwatch_instructions.txt) is being provided.

```bash
% python3 cloudwatch-titan-test.py botdev "Show me traffic going to 8.8.8.8"
{
    "inputTextTokenCount": 2499,
    "results": [
        {
            "tokenCount": 42,
            "outputText": "fields @timestamp, @logStream, srcAddr, srcPort, dstAddr, dstPort,action,packets,@message  | filter dstAddr like \"8.8.8.8\"",
            "completionReason": "FINISH"
        }
    ]
}
```