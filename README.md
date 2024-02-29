# SignLanguageRecognition-ML
Dissertation: Sign Language Recognition Application by Using Machine Learning Methods (LRCN and 3DCNN)
Nowadays, many people with hearing impairments in our society use sign language as a
communication tool. This project aims to bridge the communication gap between sign
language users and those unfamiliar with it by developing a sign language recognition
application. This project employs machine learning methods, specifically the LRCN
model and 3DCNN model. The baselines of these two methods were proposed and
modified to improve the model to achieve the project objective. Firstly, the sliding
window method was used to expand the dataset. Moreover, dropout layers and L2
regularisation were applied to reduce the overfitting. As a result, these enhancements
significantly improve the model accuracy. Among the challenges addressed by many
researchers was training a robust sign language recognition required a large dataset
with various environments. This project utilises the WLASL dataset, which is known
for its extensive vocabulary and diverse signers. For the implementation, 10 classes
were selected. A comparative analysis was also discussed among LRCN and 3DCNN
by f1-score for in-class evaluation and weighted average of f1-score for both models.
This method ensures that the model performs well to achieve the research objective
with results above 80% in each class and 95% and 94% in both models, respectively.
Additionally, resource usage was monitored, and showing that LRCN requires more
memory than 3DCNN as it needs more epochs to get high accuracy. Lastly, the model
was deployed into a web application to test with real-world data, but real-world environments’ complexity reduces the model performance. This challenge leads to further
research questions for future work. However, the project can be the prototype and
initialised the idea of a sign language recognition task.

Refference dataset: https://paperswithcode.com/dataset/wlasl
