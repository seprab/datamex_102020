USE test;
SELECT 
	author.au_id AS "AUTHOR ID",
    author.au_lname AS "LAST NAME",
    author.au_fname AS "FIRST NAME",
    SUM(sales.qty) AS "TOTAL"
FROM authors AS author
RIGHT JOIN titleauthor
ON author.au_id = titleauthor.au_id
LEFT JOIN titles
ON titleauthor.title_id = titles.title_id
LEFT JOIN sales
ON sales.title_id = titles.title_id
GROUP BY author.au_id
ORDER BY TOTAL DESC
LIMIT 3;
