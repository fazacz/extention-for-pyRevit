# -*- coding: utf-8 -*-
"""описание"""
__title__ = 'Материалы\n'
__author__ = 'SG'
import clr
clr.AddReference('System.Core')
from System.Collections.Generic import *
from Autodesk.Revit.DB import Material, ParameterType, FilteredElementCollector, BuiltInCategory, Transaction, TransactionGroup, BuiltInParameter, ElementId
import sys
from Autodesk.Revit.UI.Selection import ObjectType, ISelectionFilter
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

names = {'Аллюминий': 'Алюминий',
'Алюминий': 'Алюминий',
'Белый пластик': 'Пластик белый',
'Голубая подсветка': 'Голубая подсветка',
'Голубое стекло': 'Стекло голубое',
'Дисплей': 'Дисплей',
'Дисплей красный': 'Дисплей красный',
'Желтый пластик': 'Пластик желтый',
'ЖК экран серый': 'ЖК экран серый',
'Зеленое стекло': 'Стекло зеленое',
'Зеленый пластик': 'Пластик зеленый',
'Кнопки': 'Кнопки',
'Кнопки синие': 'Кнопки синие',
'Колеса пластик': 'Колеса пластик',
'Колеса резина': 'Колеса резина',
'Колесо': 'Колесо',
'Корпус': 'Корпус',
'Корпус2': 'Корпус2',
'Красное стекло': 'Стекло красное',
'Красный пластик': 'Пластик красный',
'Логотип': 'Логотип',
'Материал': 'Материал',
'Материал 2': 'Материал 2',
'Материал 3': 'Материал 3',
'Материал дверей': 'Материал дверей',
'Материал дисплея': 'Материал дисплея',
'Материал корпуса': 'Материал корпуса',
'Материал ручек': 'Материал ручек',
'Материал трубы': 'Материал трубы',
'Металл': 'Металл',
'Мокрый асфальт': 'Мокрый асфальт',
'Монитор': 'Монитор',
'Нержавеющая сталь': 'Нержавеющая сталь',
'Нержавеющая сталь, красная': 'Нержавеющая сталь, красная',
'Нержавеющая сталь, серебристая': 'Нержавеющая сталь',
'Ножка': 'Ножка',
'Ножки': 'Ножки',
'Ножки черные, резина': 'Ножки черные, резина',
'Оцинковка': 'Оцинковка',
'Пластик бежевый': 'Пластик бежевый',
'Пластик белый': 'Пластик белый',
'Пластик белый (светлобежевый)': 'Пластик белый (светлобежевый)',
'Пластик голубой': 'Пластик голубой',
'Пластик желтый': 'Пластик желтый',
'Пластик зеленый': 'Пластик зеленый',
'Пластик зеленый светлый': 'Пластик зеленый светлый',
'Пластик зеленый темный': 'Пластик зеленый темный',
'Пластик коричневый': 'Пластик коричневый',
'Пластик красный': 'Пластик красный',
'Пластик светлобежевый': 'Пластик светлобежевый',
'Пластик серый': 'Пластик серый',
'Пластик серый светлый': 'Пластик серый светлый',
'Пластик серый темный': 'Пластик серый темный',
'Пластик синий': 'Пластик синий',
'Пластик синий светлый': 'Пластик синий светлый',
'Пластик черный': 'Пластик черный',
'Прозрачное стекло': 'Стекло',
'Резина': 'Резина',
'Резина черная': 'Резина',
'Ручка черная, пластик': 'Пластик черный',
'Светло-серый пластик': 'Пластик серый светлый',
'Сенсорный экран, черный': 'Сенсорный экран, черный',
'Серый пластик': 'Пластик серый',
'Синее светящееся стекло': 'Синее светящееся стекло',
'Синий пластик': 'Пластик синий',
'Сталь': 'Сталь',
'Сталь золотая': 'Сталь золотая',
'Сталь нержавеющая': 'Сталь нержавеющая',
'Стекло': 'Стекло',
'Стекло цвета морской волны': 'Стекло цвета морской волны',
'Стекло черное': 'Стекло черное',
'Столешница серая': 'Столешница серая',
'Темное стекло': 'Стекло темное',
'Хром': 'Хром',
'Черная порошковая краска': 'Черная порошковая краска',
'Черное стекло': 'Стекло черное',
'Черный пластик': 'Пластик черный',
'Черный экран': 'Черный экран',
'Чугун': 'Чугун',
}

materials = FilteredElementCollector(doc)\
	.OfCategory(BuiltInCategory.OST_Materials)\
	.WhereElementIsNotElementType().ToElements()

# for mat in materials:
# 	if mat.Name == "My Material":
# 		orig = mat


t = Transaction(doc, 'Материалы')
t.Start()

types = [doc.GetElement(doc.GetElement(id).GetTypeId()) for id in uidoc.Selection.GetElementIds()]

params = []
for type in types:
	for param in type.GetOrderedParameters():
		if param.Definition.ParameterType == ParameterType.Material:
			for mat in materials:
				if mat.Name == names[param.Definition.Name]:
					break
			param.Set(mat.Id)
# types[0].GetOrderedParameters()

# for param in params:
# 	print(param.Definition.Name)

# for name in names.split('\n'):
# 	orig.Duplicate(name)

# Material.Create(doc, "My Material")

# print(materials)



t.Commit()
