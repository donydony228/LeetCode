# Write your MySQL query statement below
SELECT st.student_id, st.student_name, su.subject_name, COUNT(ex.subject_name) AS attended_exams
FROM Students st
CROSS JOIN Subjects su
LEFT JOIN Examinations ex ON st.student_id = ex.student_id AND su.subject_name = ex.subject_name
GROUP BY st.student_id, su.subject_name, st.student_id
ORDER BY st.student_id ASC