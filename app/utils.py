import random, copy
original_questions = {
    #Format is 'question':[options]
    'Taj Mahal':['Agra','New Delhi','Mumbai','Chennai'],
    'Great Wall of China':['China','Beijing','Shanghai','Tianjin'],
    'Petra':['Ma\'an Governorate','Amman','Zarqa','Jerash'],
    'Machu Picchu':['Cuzco Region','Lima','Piura','Tacna'],
    'Egypt Pyramids':['Giza','Suez','Luxor','Tanta'],
    'Colosseum':['Rome','Milan','Bari','Bologna'],
    'Christ the Redeemer':['Rio de Janeiro','Natal','Olinda','Betim']
}

questions = copy.deepcopy(original_questions)