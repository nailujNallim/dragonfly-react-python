import { useStore } from "@/store";
import { useState } from "react";

interface TodoItemProps {
  todo: {
    id: number;
    title: string;
    completed: boolean;
  };
}

const TodoItem: React.FC<TodoItemProps> = ({ todo }) => {
  const [loading, setLoading] = useState(false);

  const handleToggleComplete = () => {
    setLoading(true);
    const updatedTodo = { ...todo, completed: !todo.completed };
    setLoading(false);
  };


  return (
    <div className="flex items-center space-x-2 mb-2">
      <span
        className={`text-gray-700 flex-1 ${
          todo.completed ? "line-through" : ""
        }`}
        onClick={handleToggleComplete}
      >
        {todo.title}
      </span>

    </div>
  );
};

export default TodoItem;
