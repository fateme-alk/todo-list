/**
 * --------------------------------------------------------------------------
 * Bootstrap (v5.1.3): dom/manipulator.js
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
 * --------------------------------------------------------------------------
 */

function normalizeData(val) {
    if (val === 'true') {
        return true;
    }

    if (val === 'false') {
        return false;
    }

    if (val === Number(val).toString()) {
        return Number(val);
    }

    if (val === '' || val === 'null') {
        return null;
    }

    return val;
}

function normalizeDataKey(key) {
    return key.replace(/[A-Z]/g, (chr) => `-${chr.toLowerCase()}`);
}

const Manipulator = {
    setDataAttribute(element, key, value) {
        element.setAttribute(`data-mdb-${normalizeDataKey(key)}`, value);
    },

    removeDataAttribute(element, key) {
        element.removeAttribute(`data-mdb-${normalizeDataKey(key)}`);
    },

    getDataAttributes(element) {
        if (!element) {
            return {};
        }

        const attributes = {};

        Object.keys(element.dataset)
            .filter((key) => key.startsWith('mdb'))
            .forEach((key) => {
                let pureKey = key.replace(/^mdb/, '');
                pureKey =
                    pureKey.charAt(0).toLowerCase() +
                    pureKey.slice(1, pureKey.length);
                attributes[pureKey] = normalizeData(element.dataset[key]);
            });

        return attributes;
    },

    getDataAttribute(element, key) {
        return normalizeData(
            element.getAttribute(`data-mdb-${normalizeDataKey(key)}`),
        );
    },

    offset(element) {
        const rect = element.getBoundingClientRect();

        return {
            top: rect.top + window.pageYOffset,
            left: rect.left + window.pageXOffset,
        };
    },

    position(element) {
        return {
            top: element.offsetTop,
            left: element.offsetLeft,
        };
    },
};

export default Manipulator;
