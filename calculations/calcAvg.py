quizPercent = 0.3
testPercent = 0.5
attendancePercent = 0.2
daysToAttend = 10

testScore = 90
quizScore = 100
attendance = 9

testGrade = testScore * testPercent
quizGrade = quizScore * quizPercent
attendanceGrade = ((attendance / daysToAttend) * 100) * attendancePercent

avg = testGrade + quizGrade + attendanceGrade

print(avg)
