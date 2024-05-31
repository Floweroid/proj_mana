interface User {
    id: number;
    username: string;
    // Add other fields as needed
}

interface Habit {
    id: number;
    user: User;
    name: string;
    description?: string;
    createdAt: string; // Use ISO 8601 date format
    updatedAt: string;
    defaultTimezone: string;
    streakDisplay: number;
    totalDaysTracked: number;
}

interface HabitTrack {
    id: number;
    habit: Habit;
    date: string; // Use ISO 8601 date format
    createdAt: string;
    updatedAt: string;
    comment?: string;
}

interface HabitWithTracks {
    habit: Habit;
    tracks: HabitTrack[];
}
const user: User = {
    id: 1,
    username: 'johndoe'
};

const habit: Habit = {
    id: 1,
    user: user,
    name: 'Exercise Daily',
    description: 'Daily exercise habit to stay fit',
    createdAt: '2023-05-25T12:34:56Z',
    updatedAt: '2023-05-26T12:34:56Z',
    defaultTimezone: 'UTC',
    streakDisplay: 5,
    totalDaysTracked: 30
};

const habitTrack: HabitTrack = {
    id: 1,
    habit: habit,
    date: '2023-05-26',
    createdAt: '2023-05-26T12:34:56Z',
    updatedAt: '2023-05-26T12:34:56Z',
    comment: 'Great workout session'
};

const habitWithTracks: HabitWithTracks = {
    habit: habit,
    tracks: [habitTrack]
};
