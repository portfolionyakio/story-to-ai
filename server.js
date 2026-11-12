import express from 'express';
import { GoogleGenAI } from '@google/genai';

const app = express();
const port = process.env.PORT || 3000;
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

app.use(express.json());
app.use(express.static('public'));

app.post('/api/transform', async (req, res) => {
  try {
    const { story, style } = req.body;
    if (!story) return res.status(400).json({ error: 'Please provide a story.' });

    const prompt = `Transform this story into a ${style} experience. Break it into 3 vivid scenes with a title, visual description, and dialogue. End with 2 "What happens next?" choices.\n\nStory: "${story}"`;

    const response = await ai.models.generateContent({
      model: 'gemini-2.5-flash',
      contents: prompt
    });

    res.json({ result: response.text });
  } catch (error) {
    res.status(500).json({ error: 'Failed to transform story.' });
  }
});

app.listen(port, () => console.log('Running on port ' + port));
