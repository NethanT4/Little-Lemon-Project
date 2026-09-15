import { fireEvent, render, screen } from "@testing-library/react";
import FeedbackForm from "./FeedbackForm";

describe("Feedback Form", () => {
  test("User is able to submit the form if the score is lower than 5 and additional feedback is provided", () => {
    const score = "3";
    const comment = "The pizza crust was too thick";
    const handleSubmit = jest.fn();
    render(<FeedbackForm onSubmit={handleSubmit} />);

    fireEvent.change(screen.getByLabelText("Score:"), {
      target: { value: score },
    });

    fireEvent.click(screen.getByRole("textbox"), {
      target: { value: comment },
    });

    fireEvent.change(screen.getByRole("button", { name: /submit/i }));

    expect(handleSubmit).toHaveBeenCalledWith({
      score,
      comment,
    });
  });

  test("User is able to submit the form if the score is higher than 5, without additional feedback", () => {
    const score = "9";
    const handleSubmit = jest.fn();
    render(<FeedbackForm onSubmit={handleSubmit} />);

    fireEvent.click(screen.getByLabelText(/score:/i), {
      target: {value: score },
    });
    fireEvent.click(screen.getByRole("button", { name: /submit/i }));

    expect(handleSubmit).toHaveBeenCalledWith({
      score,
      comment: "",
    });
  });
});
