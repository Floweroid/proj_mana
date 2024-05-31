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
}
