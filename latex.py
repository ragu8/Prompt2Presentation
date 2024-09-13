from openai import OpenAI

def genrate_tex(user_prompt, model="gpt-4o"):
    system_prompt = """
\\documentclass{beamer}

% Theme setup
\\usetheme{default}
\\usepackage{graphicx}

% Color setup
\\setbeamercolor{frametitle}{bg=blue,fg=black}  % Header background blue, title color black
\\setbeamercolor{title in head/foot}{bg=blue,fg=white}

% Remove color from the footer
\\setbeamercolor{footline}{bg=,fg=black}  % No background color for the footer, set text color to black

% Logo setup (right side of the header, with fine adjustments for vertical and horizontal positioning)
\\setbeamertemplate{frametitle}{
	\\vspace{0.2cm}
	\\hbox{
		\\begin{beamercolorbox}[wd=\\paperwidth,ht=1cm,dp=0.3cm]{frametitle}
			\\hspace{0.5cm} % Adjust horizontal space from the left
			\\textbf{\\textcolor{black}{\\insertframetitle}} % Slide title in bold and black
			\\hfill
			\\raisebox{-0.1cm}{\\includegraphics[height=0.9cm]{logo.png}}  % Adjust the raisebox value to move the logo up/down
			\\hspace{0.5cm} % Adjust horizontal space from the right
		\\end{beamercolorbox}
	}
}

% Footer setup for slide number with total page number (adjustable vertical and horizontal position)
\\setbeamertemplate{footline}{
	\\hbox{
		\\hfill
		\\raisebox{0.2cm}{ % Adjust vertical positioning (positive value moves it up, negative moves it down)
			\\hspace*{11.8cm}  % Adjust horizontal positioning (move left or right)
			\\textbf{\\insertframenumber}/\\inserttotalframenumber % Add page number and total number of slides
		}
		\\hfill
	}
}

\\begin{document}
	
	% Title Slide
	\\begin{frame}
		\\title{Your Presentation Title}
		\\subtitle{Your Subtitle}
		\\author{Ragupathi M}
		\\institute{Ramanujan Computing Centre}
		\\titlepage
	\\end{frame}
	
	% Example Slide
	\\begin{frame}
		\\frametitle{Slide Title}
		Here is an example slide.
	\\end{frame}
	
	% Example Slide
	\\begin{frame}
		\\frametitle{Another Slide Title}
		Here is another example slide.
	\\end{frame}
	
\\end{document}
"""
    client = OpenAI()
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": f"You are a LaTeX maker assistant and a good researcher. Use the following LaTeX template as a base and generate a .tex file based on the user's request:\n\n{system_prompt}"},
            {"role": "user", "content": user_prompt}
        ]
    )
    content=completion.choices[0].message.content
    with open('latex.tex', 'w') as file:
        file.write(content)
    return  " Save the generated content to a file."
    
