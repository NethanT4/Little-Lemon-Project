import * as React from "react";
import "./styles.css";

export const RadioGroup = ({ onChange, selected, children }) => {
  const handleChange = (e) => {
    const newValueSelected = e.target.value;
    onChange(newValueSelected);
  };

  const RadioOptions = React.Children.map(children, (child) =>
    React.cloneElement(child, {
      checked: selected === child.props.value,
      onChange: handleChange,
    })
  );

  return <div className="RadioGroup">{RadioOptions}</div>;
};

export const RadioOption = ({ value, checked, onChange, children }) => {
  return (
    <div className="RadioOption">
      <input
        id={value}
        type="radio"
        name={value}
        value={value}
        checked={checked}
        onChange={onChange}
      />
      <label htmlFor={value}>{children}</label>
    </div>
  );
};
