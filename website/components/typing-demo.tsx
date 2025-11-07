'use client';

import { useEffect, useState } from 'react';

interface TypingDemoProps {
  text: string;
  speed?: number;
}

export function TypingDemo({ text, speed = 50 }: TypingDemoProps) {
  const [displayedText, setDisplayedText] = useState('');
  const [currentIndex, setCurrentIndex] = useState(0);
  const [showCursor, setShowCursor] = useState(true);

  useEffect(() => {
    if (currentIndex < text.length) {
      const timeout = setTimeout(() => {
        setDisplayedText(text.slice(0, currentIndex + 1));
        setCurrentIndex(currentIndex + 1);
      }, speed);
      return () => clearTimeout(timeout);
    }
  }, [currentIndex, text, speed]);

  useEffect(() => {
    const cursorInterval = setInterval(() => {
      setShowCursor((prev) => !prev);
    }, 530);
    return () => clearInterval(cursorInterval);
  }, []);

  return (
    <div className="neo-border bg-card p-6 font-mono text-lg">
      <div className="min-h-[100px]">
        <span>{displayedText}</span>
        {showCursor && <span className="text-primary">|</span>}
      </div>
    </div>
  );
}

