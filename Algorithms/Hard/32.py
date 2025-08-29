# def merge_intervals(intervals):
#     # قائمة لاحتواء الفترات المدمجة
#     merged = []

#     for interval in intervals:
#         # إذا كانت القائمة فارغة أو لا يوجد تداخل مع آخر فترة مدمجة، نضيف الفترة الحالية
#         if not merged or merged[-1][1] < interval[0]:
#             merged.append(interval)
#         else:
#             # إذا كان هناك تداخل، ندمج الفترات
#             merged[-1][1] = max(merged[-1][1], interval[1])

#     return merged

# اختبار الكود:

def merge_intervals(intervals):

    # 1. ترتيب الفترات حسب البداية
    intervals.sort()

    # 2. أول فترة نحطها في النتيجة
    merged = [intervals[0]]

    # 3. نبدأ من الثانية
    for current in intervals[1:]:
        
        # إذا في تداخل بين last و current
        if current[0] <= merged[-1][1]:
            # ندمجهم عن طريق تحديث النهاية
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            # ما في تداخل → نضيفها كفترة جديدة
            merged.append(current)

    return merged

print(merge_intervals([[1, 3], [2, 4], [5, 7], [6, 8]]))  # النتيجة: [[1, 4], [5, 8]]
print(merge_intervals([[1, 3], [2, 6], [8, 10], [9, 12]]))  # النتيجة: [[1, 4], [5, 8]]

