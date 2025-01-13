from book:

During the course of doing data analysis and modeling, a significant amount of time
is spent on data preparation: loading, cleaning, transforming, and rearranging. Such
tasks are often reported to take up 80% or more of an analyst’s time. Sometimes the
way that data is stored in files or databases is not in the right format for a particular
task. Many researchers choose to do ad hoc processing of data from one form to
another using a general-purpose programming language, like Python, Perl, R, or Java,
or Unix text-processing tools like sed or awk. Fortunately, pandas, along with the
built-in Python language features, provides you with a high-level, flexible, and fast set
of tools to enable you to manipulate data into the right form.
If you identify a type of data manipulation that isn’t anywhere in this book or
elsewhere in the pandas library, feel free to share your use case on one of the
Python mailing lists or on the pandas GitHub site. Indeed, much of the design and
implementation of pandas have been driven by the needs of real-world applications.
In this chapter I discuss tools for missing data, duplicate data, string manipulation,
and some other analytical data transformations. In the next chapter, I focus on
combining and rearranging datasets in various ways.