\documentclass[a4paper,twoside]{bth}

% BTH THESIS TEMPLATE
%--------------------
% Template version 3.4.1 -- Aug 31, 2020
%--------------------
% Please change the data below appropriately to fit your thesis.
% The data will be used to generate text in various places on the
% thesis front and inner pages.
%--------------------

% DEGREE NAME. The degree name you are submitting your thesis for.
% This must be one of the following:
% Bachelor programmes:
% Bachelor of Science in Computer Science
% Bachelor of Science in Digital Game Development
% Bachelor of Science in Software Engineering
% Master programmes:
% Master of Science in Computer Science
% Master of Science in Software Engineering
% Master of Science in Telecommunication Systems
% Civilingenjör programmes:
% Master of Science in Engineering: AI and Machine Learning
% Master of Science in Engineering: Computer Security
% Master of Science in Engineering: Game and Software Engineering
% Master of Science in Engineering: Marine Engineering
% Master of Science in Engineering: Software Engineering
% Master of Science in Industrial Management and Engineering
% Master of Science in Mechanical Engineering
\newcommand{\thesisDegree}{Higher Education Diploma in Software Engineering with emphasis in Web Programming}

% DATE. The month year when your final report was submitted.
\newcommand{\thesisMonth}{May}
\newcommand{\thesisYear}{2021}

% FACULTY.
% Must be either Computing or Engineering.
\newcommand{\faculty}{Computing}

% COURSE TIME. Course time in weeks.
% For a 15 credits course this should be 10 and
% for a 30 credits course, this should be 20 weeks.
% Note that the week figure is the same whether you work alone or in a pair.
\newcommand{\thesisWeeks}{20}

% TITLE.
\newcommand{\thesisTitle}{Centered Title in Font Times (Size 24 Bold)}

% SUBTITLE.
% If you dont have a subtitle, please delete the text in the last parenthesis.
\newcommand{\thesisSubtitle}{Centered Subtitle in Font Times (Size 16 Bold)}

% AUTHORS.
% Please replace with your first name(s) and last name(s). There can be several of each.
\newcommand{\authorFirst}{Firstname1 Lastname1}
\newcommand{\authorFirstMail}{...@student.bth.se}
% If there is no second author, please delete the texts in the last parentheses.
\newcommand{\authorSecond}{Firstname2 Lastname2}
\newcommand{\authorSecondMail}{...@student.bth.se}

% SUPERVISOR.
% Please replace with title, first and last names of your academic supervisor.
\newcommand{\super}{Title Firstname Lastname}
% Please replace with the name of the department of your academic supervisor, e.g.,
% Computer Science, Mechanical Engineering, etc.
\newcommand{\superAffiliation}{Department}

% PACKAGES AND COMMANDS START
%----------------------------
% please do not delete or change anything before the END of this section
\usepackage{amsmath}
\usepackage{mathenv}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{textcomp}
\usepackage{longtable}
\usepackage{multirow}
\usepackage{nameref}
\usepackage{booktabs}
\usepackage{pifont}
\usepackage{changepage}
\usepackage{listings}
\usepackage{url}
\usepackage{xspace}
\usepackage{xtab}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{enumitem}
\usepackage[sort&compress]{natbib}
\setcitestyle{numbers,square,comma}
\usepackage[color=blue!10,textsize=footnotesize,textwidth=25mm]{todonotes}
\DeclareGraphicsExtensions{.pdf}

\newtheorem{lem}{\textsc{Lemma}}[chapter]
\newtheorem{thm}{\textsc{Theorem}}[chapter]
\newtheorem{prop}{\textsc{Proposition}}[chapter]
\newtheorem{post}{Postulate}[chapter]
\newtheorem{corr}{\textsc{Corollary}}[chapter]
\newtheorem{defs}{\textsc{Definition}}[chapter]
\newtheorem{cons}{\textsc{Constraint}}[chapter]
\newtheorem{ex}{\textbf{Example}}[chapter]
\newtheorem{qu}{\textbf{Question}}[chapter]
% -------------------------
% PACKAGES AND COMMANDS END

% DOCUMENT BEGINS HERE
\begin{document}

\pagestyle{plain}
\pagenumbering{roman}

% THESIS FRONT PAGE (please do not change)
% ----------------------------------------
{\pagestyle{empty}
\changepage{3cm}{1cm}{-0.5cm}{-0.5cm}{}{-1.5cm}{}{}{}
\noindent
\begin{tabular}{@{}p{0.75\textwidth} p{0.25\textwidth}}
\thesisDegree & \hfill\multirow{3}{\*}{\bthcsnotextlogo{3cm}} \\
\thesisMonth \ \thesisYear & \\
\end{tabular}

%\begin{center}
\center
\vspace {7.5cm}
{\Huge\textbf{\thesisTitle}}

\vspace {0.5cm}
{\Large\textbf{\thesisSubtitle}}

\vspace{2cm}
{\Large\textbf{\authorFirst}}

\vspace{0.3cm}
{\Large\textbf{\authorSecond}}

\vspace\*{\fill}

\noindent\makebox[\linewidth]{\rule{\textwidth}{1pt}}
Faculty of \faculty, Blekinge Institute of Technology, 371 79 Karlskrona, Sweden
%\end{center}

\clearpage
} % Back to \pagestyle{plain}
% ----------------------------------------

% THESIS INNER PAGE (please do not change)
% ----------------------------------------
{\pagestyle{empty}
\changepage{3cm}{1cm}{-0.5cm}{-0.5cm}{}{-1.5cm}{}{}{}

{\small
\noindent
This thesis is submitted to the Faculty of \faculty\ at Blekinge Institute
of Technology in partial fulfilment of the requirements for the degree of
\thesisDegree. The thesis is equivalent to \thesisWeeks\ weeks of full time studies.

\vspace{1cm}

\noindent
The authors declare that they are the sole authors of this thesis and that they have
not used any sources other than those listed in the bibliography and identified as references.
They further declare that they have not submitted this thesis at any other institution to
obtain a degree.
}

\vspace{10cm}

\noindent
\textbf{Contact Information:} \\
Author(s): \\
\authorFirst \\
E-mail: \authorFirstMail \\
\\
\authorSecond \\
E-mail: \authorSecondMail

\vspace{2cm}

\noindent
University advisor: \\
\super \\
Department of \superAffiliation

\vspace\*{\fill}

\noindent
\begin{tabular}{@{}p{0.5\textwidth} l c l}
Faculty of \faculty & Internet & : & www.bth.se \\
Blekinge Institute of Technology & Phone & : & +46 455 38 50 00 \\
SE--371 79 Karlskrona, Sweden & Fax & : & +46 455 38 50 57 \\
\end{tabular}
\clearpage
} % Back to \pagestyle{plain}
% ----------------------------------------

\setcounter{page}{1}

%%%%%%%%%%%%%%%%%%%%%%%%
% YOUR TEXTS START HERE
%%%%%%%%%%%%%%%%%%%%%%%%

% ABSTRACT IN ENGLISH
% -------------------
\abstract
Most readers will turn first to the abstract of your thesis. Use it as an opportunity to spur the reader's interest. The abstract should highlight the main points from your work, especially the thesis' problems statement, methods, findings and conclusions. However, the abstract does not need to cover every aspect of your work. The main objective is to give the reader a good idea of what the thesis is about.

The abstract should be completed towards the end, when you are able to overview your project as a whole. It is nevertheless a good idea to work on a draft continuously. Writing a good abstract can be difficult, since it should only include the most important points of your work. But this is also why working on your abstract can be so useful -- it forces you to identify the key elements of your degree project.

Structured abstracts have several advantages for authors and readers. They help readers to quickly find information in an abstract and also guide authors in summarizing the content of their manuscripts precisely. Below you find the main components of a structured abstract.

\noindent
\textbf{Background.} ... \newline
\textbf{Objectives.} ... \newline
\textbf{Methods.} ... \newline
\textbf{Results.} ... \newline
\textbf{Conclusions.} ...

\vspace{1cm}
% You can list up to 5 keywords, at most 2 appearing in the title;
% starts 1 line below the abstract.
\noindent
\textbf{Keywords:} Up to 5 keywords, at most 2 of these should appear in the title. Starts 1 line below the abstract.

\cleardoublepage
% -------------------

% ABSTRACT IN SWEDISH
% -------------------
\sammanfattning
\todo[inline]{An abstract in Swedish is only needed for ``civilingenjör'' theses.}
\noindent
\textbf{Bakgrund.} ... \newline
\textbf{Syfte.} ... \newline
\textbf{Metod.} ... \newline
\textbf{Resultat.} ... \newline
\textbf{Slutsatser.} ...

\vspace{1cm}
% You can list up to 5 keywords, at most 2 appearing in the title;
% starts 1 line below the abstract.
\noindent
\textbf{Nyckelord:} Upp till 5 nyckelord, varav maximal 2 bör förekomma i titeln. Börjar 1 rad under sammanfattningen.

\cleardoublepage
% -------------------

% ACKNOWLEDGEMENTS
% -------------------
\acknowledgments % Optional, comment out this part if not needed
\noindent
Here you can add your acknowledgements.

\cleardoublepage
% -------------------

% TABLE OF CONTENTS PAGES (generated by LaTeX using the command(s) below)
% You should uncomment the commands you need.
\tableofcontents
%\listoffigures % in case you have them
%\listoftables % in case you have them
%\listofalgorithms % in case you have them

\cleardoublepage
\pagestyle{headings}
\pagenumbering{arabic}

\chapter{Preface}
In the final thesis, you need to delete this chapter. Here, we specify some preliminaries that are valid for the whole thesis. Specific tips and guidelines are provided in the following chapters.

\section{On supervisor feedback}
When you prepare the thesis draft, consider that feedback from supervisors cannot be requested outside regular office hours, \emph{even though submission deadlines might be scheduled on a Sunday}. Hence, avoid requesting feedback on Friday afternoon before the submission deadline or even on the weekend. Supervisors should give feedback in a reasonable time-frame. Planning and adhering to internal draft deadlines help you to receive quality feedback, on time.

\section{On formatting}
Please note that the chapter names and the chapter structure in this template are
just suggestions. There is no ``one-size-fits-all'' structure for all types of theses.
You need to use chapter, section and subsection headers that are adapted to your
particular topic.
%Preferably, you should formulate your headers (and lists in general)
%in so-called parallel (grammatical) form or structure.
%If you do not remember what that means, now is the time to refresh your memory.

Headers as well as regular paragraphs should start at the left margin of a page and
be aligned left and right, as in the paragraphs shown here (i.e. unlike in Word).
There should be no white-space between paragraphs, but the first line of each
paragraph should be indented, except for the first paragraph following a section-,
subsection-, or sub-subsection header.

Please make sure to get your citations and references correct and consistent.
Just copying/pasting information from GoogleScholar or bibliographic databases is insufficient,
since the citation information, in particular from GoogleScholar, is often incorrect and/or incomplete.
Please see the course literature, e.g., \cite{berndtsson2007thesis,evans2014write,glasman2010science,zobel2014writing}
for more information about the handling of citations and references.

\todo[inline]{Notes like this can be useful for your own comments. You can hide all of them
at once by adding \texttt{disable} to the list of parameters to the command
\texttt{\textbackslash usepackage[color=blue!10,textsize=footnotesize,textwidth=25mm]{todonotes}}.}

\section{On thesis structure and length}
A thesis typically follows the structure already provided in this document. However, depending on the content and nature of a thesis, you may find it appropriate to deviate from that structure when reporting results and analysis and separate them into two chapters. In general, the contents of results, analysis and discussion are the following:
\begin{itemize}
\item Results: objective results (data) without analysis and interpretation
\item Analysis: objective analysis/interpretation of the results, that is based solely on the collected data
\item Discussion: interpretation of the results and analysis within the context of the body of knowledge (external to your thesis)
\end{itemize}

It often makes sense to combine results and analysis into one chapter in order to avoid redundancy. However, there are scenarios where it makes sense to separate results from analysis. For example, when you designed a study with two separate research methods and one research question requires you to analyse the results in combination. Then it may make sense to report all results in one chapter and the analysis answering the research questions in another.

Table~\ref{tab:pl} provides suggestions for a range of page lengths for each thesis chapter. Please note that these are rough estimates for your orientation. The chapters shall however not fall below the minimum length estimates. The complete thesis text, excluding preliminaries, references and appendices, shall not exceed 80 pages.

\begin{table}[htb]
\centering
\begin{tabular}{lc}
\toprule
Chapter & Min--Max pages \\
\midrule
\nameref{chp:introduction} & 3--5 \\
\nameref{chp:relatedwork} & 3--7 \\
\nameref{chp:method} & 7--15 \\
\nameref{chp:results} & 8--20 \\
\nameref{chp:discussion} & 8--15 \\
\nameref{chp:conclusions} & 5--10 \\
\midrule
TOTAL & 34--72 \\
\bottomrule
\end{tabular}
\caption{Chapter length estimates}
\label{tab:pl}
\end{table}

In the following, each chapter provides some guidance\footnote{Adapted from
\begin{itemize}[nolistsep]
\item \url{https://sokogskriv.no/en/writing/structure-and-argumentation/structuring-a-thesis/}
\item \url{https://thesisguide.org/2014/10/13/thesis-architecture/}
\item \url{https://guidetogradschoolsurvival.wordpress.com/2011/04/08/how-to-write-related-work/}
\item \url{https://dissertationgenius.com/12-steps-write-effective-discussion-chapter/}
\end{itemize}} on what is expected as content. Please refer to the evaluation rubrics in the thesis guidelines document \cite{guidelines_DP-BTH} to assess yourself regarding the degree to which your content fulfils the criteria.

%------------------------------
% THE ACTUAL THESIS STARTS HERE
% The chapters below are just suggestions and need to be adapted to your topic.

\chapter{Introduction}
\label{chp:introduction} % labels are used for cross references

\section{On the content}
Your introduction has two main purposes: 1) to give an overview of the main points of your thesis, and 2) to awaken the reader's interest. It is recommended to rewrite the introduction one last time when the writing is done, to ensure that it connects well with your conclusion.

\emph{Tip}: For a nice, stylistic twist you can reuse a theme from the introduction in your conclusion. For example, you might present a particular scenario in one way in your introduction, and then return to it in your conclusion from a different -- richer or contrasting -- perspective.

The introduction should include:
\begin{itemize}
\item The background for your choice of theme
\item A problem statement that defines the scope of your thesis
\item A schematic outline of the remainder of your thesis
\end{itemize}

\subsection{Background}
The background sets the general tone for your thesis. It should make a good impression and convince the reader why the theme is important and why your approach is appropriate and relevant. Even so, it should be no longer than necessary.

What is considered a relevant background depends on your field and its traditions. Background information might be historical in nature, or it might refer to previous research or practical considerations. You can also focus on a specific text, thinker or problem.

Academic writing often means having a discussion with yourself (or some imagined opponent). To open your discussion, there are several options available. You may, for example:
\begin{itemize}
\item Refer to a contemporary event
\item Outline a specific problem, a case study or an example
\item Review the relevant research/literature to demonstrate the need for this particular type of research
\end{itemize}

You can also define here the fundamental concepts your thesis builds on. Your thesis implements a new type of parser generator and uses the term non-terminal symbol a lot? Here is where you define what you mean by it. The key to this chapter is to keep it very, very short. Whenever you can, don't reinvent a description for an established concept, but reference a text book or paper instead.

\emph{Tip}: Do not spend too much time on your background and opening remarks before you have started with the main text.

\subsection{Defining the scope of your thesis}
One of the first tasks of a researcher is defining the scope of a study, i.e. its area (theme, field) and the amount of information to be included. Narrowing the scope of your thesis can be time-consuming, but the more you limit the scope, the more interesting a thesis becomes and the easier it will be for you to decide what is relevant to include and what can be excluded. This is because a narrower scope lets you clarify the problem and study it at greater depth, whereas very broad research questions only allow a superficial treatment.

Sometimes you can also clarify the scope by providing an overall research question or a hypothesis that will be tested. More specific sub-questions~/~hypotheses should be formulated and motivated in the \nameref{chp:method} chapter.

\subsection{Outline}
The outline gives an overview of the main points of your thesis. It clarifies the structure of your thesis and helps you find the correct focus for your work. The outline can also be used in supervision sessions, especially in the beginning. You might find that you need to restructure your thesis. Working on your outline can then be a good way of making sense of the necessary changes. A good outline shows how the different parts relate to each other, and is a useful guide for the reader.

\chapter{Related Work}
\label{chp:relatedwork}
\section{On the content}
This chapter collects descriptions of existing works that are related to your work. Related, in this sense, means that it aims to solve the same (or similar) problem or uses the same approach to solve a different problem. This chapter typically reads like a structured list. Each list item summarizes a piece of work (typically a research paper) briefly and \emph{explains the relation to your work}. This last part is absolutely crucial: the reader should not have to figure out the relation him- or herself. Is your work better from some perspective? More generalisable? More performant? Simpler? It is OK if it is not, but you should tell the reader.

A few suggestions to make writing your related work section easier:
\begin{itemize}
\item Every time you read a paper, write a short summary of the paper and highlight important sections. This way you can read your own recap of the paper to decide if it's applicable instead of relying on the abstract.
\item Use the reference section of the papers you read to search for other papers to read. If a paper is closely related to your topic, then likely the papers they reference are papers that are also closely related to your topic and you should read them.
\item When writing a paragraph on a paper, make sure you can answer the question `how does this relate to my work?'' If you can't, consider not including it.
    \item Think about the `bigger picture'' of the works you present/summarize. In which ways are they similar or different?
\end{itemize}

\emph{Tip}: End the chapter with a summary that makes clear how your works fits into the works presented and which gaps it fills.

\chapter{Method}
\label{chp:method}
\section{On the content}
Here you specify and motivate your research questions (and relate them to the main research question if you have defined one in the introduction). An important property of a research question is that it can be answered. If not, you have probably come up with a theme or a field, not a question. You can find many guidelines online (e.g., this one\footnote{\url{http://www.robertfeldt.net/advice/guide_to_creating_research_questions.pdf}}) on how to formulate good research questions.

Some tips:
\begin{itemize}
\item Use interrogative words: how, why, which (factors/situations), in which ways, etc.
\item Some questions are closed and only invoke concrete/limited answers. Others will open up for discussions and different interpretations.
Asking `What?'' is a more closed question than asking `How?'' or `In what way?'' Asking `Why'' means you are investigating the causes of a phenomenon. Studying causality is methodologically demanding.
\item Feel free to pose partially open questions that allow discussions of the overall theme, e.g., `In what way\dots''; `How can we understand [a particular phenomenon]?''
\item Do not use research questions that are answered by just `yes'' or `no'', except when you have a specific hypothesis that you are going to test.
\item Avoid questions stating that you want ``to know'' something. It is very unlikely that you get to know something definitely after your degree project.
\end{itemize}

The method chapter should not iterate the contents of methodology handbooks. You also do not need to describe the differences between quantitative and qualitative methods, or list all different kinds of validity and reliability. Such general descriptions are only meaningful when you need them to motivate the approach you have taken.

What you \emph{must} do is to show how your choice of design and research method is suited to answering your research question(s). A good approach to motivate your choice is to compare the properties, characteristics and features of different research methods, illustrating why a particular method is (not) well suited to answer a particular research question. You should try to identify reasonable (but not all) research methods, that have at least the potential to be considered as alternatives. In addition, you should demonstrate that you have given due consideration to the validity and reliability of your chosen method. By `showing'' instead of `telling'', you demonstrate that you have understood the practical meaning of these concepts. This way, the method section is not only able to tie the different parts of your thesis together, it also becomes interesting to read!

\begin{itemize}
\item Show the reader what you have done in your study, and explain why. How did you collect the data? Which options became available through your chosen approach (and which not)?
\item What were your working conditions? What considerations did you have to balance?
\item Tell the reader \emph{what you did to increase the validity} of
your research. E.g., what can you say about the reliability in data
collection? How do you know that you have actually investigated what you
intended to investigate? What conclusions can be drawn on this basis?
Which conclusions are certain and which are more tentative? Can your
results be applied in other areas? Can you generalise? If so, why? If
not, why not?
\item You should aim to describe weaknesses as well as strengths. An excellent thesis distinguishes itself by defending -- and at the same time criticising -- the choices made. Being self-critical increases trustworthiness.
\end{itemize}

\chapter{Results and Analysis}
\label{chp:results}
\section{On the content}
Your results and analysis, along with your discussion, will form the highlight of your thesis. This is where you report your findings and present them in a systematic manner. The expectations of the reader have been built up through the other chapters, make sure you fulfill these expectations.

To analyse means to distinguish between different types of phenomena -- similar from different. Importantly, by distinguishing between different phenomena, your theory is put to work. Precisely how your analysis should appear, however, is a methodological question. Finding out how best to organise and present your findings may take some time. A good place to look for examples and inspiration is repositories for master theses.

\chapter{Discussion}
\label{chp:discussion}
\section{On the content}
In many theses the discussion is the most important section. Make sure that you allocate enough time and space for a good discussion. This is your opportunity to show that you have understood the significance of your findings and that you are capable of applying theory in an independent manner.

The discussion will consist of argumentation. In other words, you investigate a phenomenon from several different perspectives. To discuss means to question your findings, and to consider different interpretations. Here are a few examples of formulations that signal argumentation:

\begin{itemize}
\item On the one hand \dots and on the other \dots
\item However \dots
\item \dots it could also be argued that \dots
\item Another possible explanation may be \dots
\end{itemize}

Here are 12 steps to keep in mind when writing your Discussion chapter:
\begin{enumerate}
\item Always try to structure your Discussion chapter from the `specific'' to the `general'': expand and transition from the narrow confines of your study to the general framework of your discipline.
\item Make a consistent effort to stick with the same general tone of the introduction. This means using the same key terms, the same tense, and the same point of view as used in your introduction.
\item Start by rewriting your research questions and re-stating your hypothesis (if any) that you previously posed in your introduction or method. Then declare the answers to your research questions -- make sure to support these answers with the findings/results of your thesis.
\item Continue by explaining how your results relate to the expectations of your study and to the literature. Clearly explain why these results are acceptable and how they consistently fit in with previously published knowledge about the subject. Make sure to use relevant citations.
\item Make sure to give the proper attention to all the results relating to your research questions, this is regardless of whether or not the findings were statistically significant.
\item Don't forget to tell your audience about the patterns, principles, and key relationships shown by each of your major findings and then put them into perspective. The sequencing of this information is important: 1) state the answer, 2) show the relevant results and 3) cite the work of credible sources. When necessary, point the audience to figures and/or graphs to ``enhance'' your argument.
\item Make sure to defend your answers. Try to do so in two ways: by explaining the validity of your answer and by showing the shortcomings of others' answers. You will make your point of view more convincing if you give both sides to the argument.
\item Also make sure to identify conflicting data in your work. Make a good point of discussing and evaluating any conflicting explanations of your results. This is an effective way to win over your audience and make them sympathetic to any true knowledge your study might have to offer.
\item Make sure to include a discussion of any unexpected findings. When doing this, begin with a paragraph about the finding and then describe it. Also identify potential limitations and weaknesses inherent in your study. Then comment on the importance of these limitations to the interpretation of your findings and how they may impact their validity. Do not use an apologetic tone in this section. Every study has limitations.
\item Conduct a brief summary of the principal implications of your findings (do this regardless of any statistical significance). Make sure to provide 1--2 recommendations for potential research in the future.
\item Show how the results of your study and their conclusions are significant and how they impact our understanding of the problem(s) that your thesis examines.
\item On a final note, discuss everything that is relevant \emph{but be brief, specific, and to the point}.
\end{enumerate}

You should also think about the potential wider consequences of your results. Do they have an impact on society? What are possible ethical consequences of your findings? Does your work have an impact on sustainability (in whatever dimension)?

\chapter{Conclusions and Future Work}
\label{chp:conclusions}
\section{On the content}
The final section of your thesis may take one of several different forms. Some theses need a conclusion, while for others a summing up will be appropriate. The decisive factor will be the nature of your thesis statement and/or research question.

Open research questions cannot always be answered, but if a definite answer is possible, you \emph{must} provide a conclusion. The conclusion should answer your research question(s). Remember that a negative conclusion is also valid.

A summing up should repeat the most important issues raised in your thesis (particularly in the discussion), although preferably stated in a (slightly) different way. For example, you could frame the issues within a wider context.

\subsection{Placing your thesis in perspective}
In the final section you should place your work in a wider, academic perspective and determine any unresolved questions. During the work, you may have encountered new research questions and interesting literature which could have been followed up. At this point, you may point out these possible developments, while making it clear for the reader that they were beyond the scope of your current project.

\begin{itemize}
\item Briefly discuss your results through a different perspective. This will allow you to see aspects that were not apparent to you at the project preparation stage.
\item Highlight alternative research questions that you have found in the source materials used in the project.
\item Show how others have placed the subject area in a wider context.
\item If others have drawn different conclusions from yours, this will provide you with ideas of new ways to view the research question.
\item Describe any unanswered aspects of your project.
\item Specify potential follow up and new projects.
\end{itemize}

\subsection{A thesis should ``bite itself in the tail''}
There should be a strong connection between your conclusion and your introduction. All themes and issues that you raised in your introduction must be referred to again in one way or another. If you find out at this stage that your thesis has not tackled an issue that you raised in the introduction, you should go back to the introduction and delete the reference to that issue. An elegant way to structure the text is to use the same textual figure or case in the beginning as well as in the end. When the figure returns in the final section, it will have taken on a new and richer meaning through the insights you have encountered, created in the process of writing.

% All references are in a separate file: thesis-refs.bib
\setlength{\bibsep}{4pt}
\bibliography{thesis-refs}
\bibliographystyle{IEEEtranS}

\appendix
\chapter{Supplemental Information}

% DO NOT CHANGE BELOW
% This part makes sure that the last page is even with BTH-logo.
% -------------------
\cleardoublepage
\thispagestyle{empty}
\vspace*{\fill}
\clearpage{\thispagestyle{empty}}
\changepage{3cm}{1cm}{-0.5cm}{-0.5cm}{}{-1.5cm}{}{}{}
\vspace*{\fill}
\center

{\bthcsnotextlogo{3cm}}
\\
\noindent\makebox[\linewidth]{\rule{\textwidth}{1pt}}
Faculty of \faculty, Blekinge Institute of Technology, 371 79 Karlskrona, Sweden
% -------------------

\end{document}
