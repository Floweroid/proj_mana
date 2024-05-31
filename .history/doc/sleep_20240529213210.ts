interface User {
    id: number;
    username: string;
    // Add other fields as needed
}

interface Sleep {
    id: number;
    user: User;
    name: string;
    description?: string;
    createdAt: string; // Use ISO 8601 date format
    updatedAt: string;
    defaultTimezone: string;
    streakDisplay: number;
    totalDurationTracked: string; // Duration as string, e.g., "PT8H30M"
}

interface SleepTrack {
    id: number;
    sleep: Sleep;
    date: string; // Use ISO 8601 date format
    createdAt: string;
    updatedAt: string;
    comment?: string;
    duration: string; // Duration as string, e.g., "PT8H30M"
}

interface SleepWithTracks {
    sleep: Sleep;
    tracks: SleepTrack[];
};

const user: User = {
    id: 1,
    username: 'johndoe'
};

const sleep: Sleep = {
    id: 1,
    user: user,
    name: 'Sleep',
    description: 'Tracking my sleep hours',
    createdAt: '2023-05-25T12:34:56Z',
    updatedAt: '2023-05-26T12:34:56Z',
    defaultTimezone: 'UTC',
    streakDisplay: 5,
    totalDurationTracked: 'PT40H' // 40 hours of total sleep tracked
};

const sleepTrack: SleepTrack = {
    id: 1,
    sleep: sleep,
    date: '2023-05-26',
    createdAt: '2023-05-26T12:34:56Z',
    updatedAt: '2023-05-26T12:34:56Z',
    comment: 'Good sleep',
    duration: 'PT8H' // 8 hours sleep
};

const sleepWithTracks: SleepWithTracks = {
    sleep: sleep,
    tracks: [sleepTrack]
};
