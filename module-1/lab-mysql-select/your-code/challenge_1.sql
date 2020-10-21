USE test;
/*"AUTHOR ID", "LAST NAME", "FIRST NAME", "TITLE", "PUBLISHER"*/
SELECT 
	author.au_id AS "AUTHOR ID",
    author.au_lname AS "LAST NAME",
    author.au_fname AS "FIRST NAME",
    titles.title AS "TITLE",
    publishers.pub_name AS "PUBLISHER"
FROM authors AS author
RIGHT JOIN titleauthor
ON author.au_id = titleauthor.au_id
LEFT JOIN titles
ON titleauthor.title_id = titles.title_id
LEFT JOIN publishers
ON titles.pub_id = publishers.pub_id;

