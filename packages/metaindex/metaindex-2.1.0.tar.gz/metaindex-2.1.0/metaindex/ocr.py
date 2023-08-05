"""OCR facilities"""
import shutil
import subprocess
import io

try:
    from PIL import Image
except ImportError:
    Image = None

from metaindex import logger


Tesseract = shutil.which('tesseract')


_fatal_logged = False


class OCRResult:
    """The outcome of an OCR run
    """
    def __init__(self, **kwargs):
        self.exc = kwargs.get('exc', None)
        """An exception that occured during the OCR run"""
        self.success = kwargs.get('success', False)
        """Whether or not the OCR run was successful"""
        self.fulltext = kwargs.get('fulltext', None)
        """The fulltext that was extracted"""
        self.language = kwargs.get('language', None)
        """What language was used for extraction"""
        self.confidence = kwargs.get('confidence', None)
        """The numerical confidence value """

    def __bool__(self):
        return self.success

    def __str__(self):
        return self.fulltext

    def __lt__(self, other):
        return self.comparator() < other.comparator()

    def comparator(self):
        """The values to use for comparisons between OCR results"""
        return [not self.success, self.confidence]


class OCRFacility:
    """API of OCR facilities
    """
    def __init__(self, accept_list=None, **kwargs):
        """:param anguages: list of languages to try when running OCR"""
        self.accept_list = accept_list
        self.languages = kwargs.get('languages', ['eng', 'deu'])

    def run(self, image):
        """Execute an OCR run on this image

        Returns an instance of OCRResult
        """
        raise NotImplementedError()


class Dummy(OCRFacility):
    """Dummy OCR facility

    Doesn't do anything, but provides the API.
    """
    def run(self, _):
        return OCRResult(success=False)


if Tesseract is None:
    class TesseractOCR(OCRFacility):
        def run(self, image):
            global _fatal_logged
            if not _fatal_logged:
                logger.fatal("Tesseract is not installed. Cannot run OCR")
                _fatal_logged = True
            return super().run(image)

else:
    class TesseractOCR(OCRFacility):
        def run(self, image):
            results = [self.do_run(image, lang) for lang in self.languages]
            best = OCRResult(success=False)
            if len(results) > 0:
                results.sort()
                best = results[0]
            return best

        def do_run(self, image, lang):
            tess = None
            result = OCRResult(success=False, fulltext='', confidence=0, language=lang)
            try:
                imagedata = io.BytesIO()
                image.save(imagedata, "JPEG")
                imagedata.seek(0)
                process = subprocess.run([Tesseract, '-', '-'],
                                         input=imagedata.getbuffer(),
                                         capture_output=True,
                                         check=False)
                if process.returncode == 0:
                    result.fulltext = str(process.stdout, 'utf-8').strip()
                    result.confidence = 1
                    result.success = True
            except KeyboardInterrupt:
                raise
            except Exception as exc:
                result.exc = exc
            finally:
                if tess is not None:
                    tess.clear()
            return result
