from sentence_transformers import SentenceTransformer, util

def segment_text(text):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    sentences = text.split(". ")
    embeddings = model.encode(sentences)
    clusters = util.community_detection(embeddings)
    chapters = []
    for cluster in clusters:
        chapter = " ".join([sentences[idx] for idx in cluster])
        chapters.append(chapter)
    return chapters

if __name__ == "__main__":
    sample_text = "Your sample text here."
    print(segment_text(sample_text))
