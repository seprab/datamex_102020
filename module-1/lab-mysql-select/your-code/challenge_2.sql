USE test;
SELECT 
	author.au_id AS "AUTHOR ID",
    author.au_lname AS "LAST NAME",
    author.au_fname AS "FIRST NAME",
    publishers.pub_name AS "PUBLISHER",
    COUNT(author.au_id) AS "TITLE COUNT"
    
FROM authors AS author
RIGHT JOIN titleauthor
ON author.au_id = titleauthor.au_id
LEFT JOIN titles
ON titleauthor.title_id = titles.title_id
LEFT JOIN publishers
ON titles.pub_id = publishers.pub_id
GROUP BY author.au_id;

