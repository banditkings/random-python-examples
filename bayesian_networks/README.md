# A Gentle Introduction to Bayesian Networks in Python with `pomegranate` for Finance Analysts

## Introduction

Corporate finance loves its cycles. You're either 'closing the books' (i.e. the quarter-end ''**Close** process') and reporting on past performance or you're engaged in some planning or forecasting activity for the future. 

Understanding past performance *should* be a routine and robust procedure, but when it comes to *planning* there's plenty of discretion left to the analyst. It ends up being a mix of business acumen and org politics (especially if incentives are on the line). If you're a 'blank spreadsheet' kind of team that's redoing your forecast every cycle, you'll typically be following one of two approaches:

| Method | What is it | Example
| --- | ---- | ----|
|*Bottoms-Up*| Starting from key drivers of the business and the latest data from the close process, calculate how each driver is expected to result in financial performance. | Add up expected attrition and hiring to calculate expected headcount for engineering personnel, and then use that headcount and average salary to arrive at a personnel spending line item. |
|*Tops-Down*| Starting from some high-level, overarching assumptions and then applying some judgment|Take last quarter's forecast and increase it by 5% because some higher-paid person said so

Not very scientific, is it? Analysts intuitively want to incorporate new information from the **Close** process, but more often than not I see folks using the 'blank spreadsheet' approach. 

## How Should We Update Our Plans?

Today I want to remind folks about a little theorem that you've likely encountered before: **Bayes Theorem**:

$$
\overbrace{\color{purple} P(A|B)}^{\textbf{\color{purple} Posterior }} = 
\frac{
	\overbrace{\color{blue} P(B|A)} ^ {\textbf{ \color{blue} Likelihood }} 
	\overbrace{\color{red} P(A)}^{\textbf{\color{red} Prior}} }
	{\underbrace{\color{green} P(B)}_{\textbf{\color{green} Evidence}}
}
$$

And now most folks will go 'aha' and recall memorizing this theorem and using the gold 'plug and chug' technique to grind out some calculations from an old class, and then promptly forgot about it as soon as the test was over. But this theorem can be extended to help you understand how you can take your subjective beliefs about something and *how much* these beliefs should change when you're given new evidence.




