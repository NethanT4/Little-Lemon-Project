function DessertsList({ data }) {
  const desserts = data
    .filter((dessert) => dessert.calories <= 500)
    .sort((a, b) => a.calories - b.calories);
  
  return (
    <ul>
      {desserts.map((dessert) => (
        <li key={dessert.name}>
          {dessert.name} - {dessert.calories} cal
        </li>
      ))}
    </ul>

  );
}

export default DessertsList;
