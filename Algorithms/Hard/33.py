def largestRectangleArea(heights):
    # نضيف عمود ارتفاعه صفر في النهاية، علشان نضمن نحسب كل المساحات
    heights.append(0)

    # هذا المكدس بيحفظ إندكسات الأعمدة
    stack = []

    # أكبر مساحة نقدر نوصل لها
    max_area = 0

    # نمر على كل عمود واحد واحد
    for i in range(len(heights)):
        # طالما المكدس مو فاضي والارتفاع الحالي أقل من اللي قبله
        while stack and heights[i] < heights[stack[-1]]:
            # نخرج آخر عمود من المكدس ونحسب مستطيل منه
            height = heights[stack.pop()]

            # نحدد العرض:
            # إذا المكدس فاضي، يعني هذا العمود الأقل من الكل → العرض = i
            # إذا مو فاضي، العرض = المسافة بين العمود الحالي واللي في أعلى المكدس بعد الحذف
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1

            # نحسب المساحة ونحدث أكبر مساحة
            area = height * width
            max_area = max(max_area, area)

        # نضيف العمود الحالي للمكدس
        stack.append(i)

    return max_area


heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))  # الناتج: 10
