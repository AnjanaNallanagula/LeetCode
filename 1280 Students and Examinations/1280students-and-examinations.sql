SELECT STU.student_id, STU.student_name, SUB.subject_name, COUNT(E.student_id) AS attended_exams
FROM Students STU CROSS JOIN Subjects SUB
LEFT OUTER JOIN Examinations E ON
(STU.student_id = E.student_id AND SUB.subject_name = E.subject_name)
GROUP BY STU.student_id, SUB.subject_name
ORDER BY STU.student_id, SUB.subject_name;